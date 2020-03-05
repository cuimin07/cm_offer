'''
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]

提示：
节点总数 <= 10000
'''

#答：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        # if not root: return []
        # stack = [([root.val], root)]
        # res = []
        # while stack:
        #     tmp, node = stack.pop()
        #     if not node.right and not node.left and sum(tmp) == sum_:
        #         res.append(tmp)
        #     if node.right:
        #         stack.append((tmp + [node.right.val], node.right))
        #     if node.left:
        #         stack.append((tmp + [node.left.val], node.left))
        # return res
        def helper(root, tmp, sum_):
            if not root:
                return 
            if not root.left and not root.right and sum_ - root.val == 0:
                tmp += [root.val]
                res.append(tmp)
            helper(root.left, tmp + [root.val], sum_ - root.val) 
            helper(root.right, tmp + [root.val], sum_ - root.val) 
        res = []
        helper(root, [], sum_)
        return res
