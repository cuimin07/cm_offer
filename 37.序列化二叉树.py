'''
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 
你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5
序列化为 "[1,2,3,null,null,4,5]"
'''

#答：
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper1(root, string):
            if root is None: string += 'None,'
            else:
                string += str(root.val) + ','
                string = helper1(root.left, string)
                string = helper1(root.right, string)
            return string
        
        return helper1(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper2(l):
            if l[0] == 'None': 
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = helper2(l)
            root.right = helper2(l)
            return root

        data_list = data.split(',')
        root = helper2(data_list)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
