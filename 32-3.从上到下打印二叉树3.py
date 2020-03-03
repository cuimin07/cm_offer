'''
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [20,9],
  [15,7]
]

提示：
节点总数 <= 1000
'''

#答：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        deque = [root]
        res = []
        times = 1
        while deque:
            out, temp = [], []
            while deque:
                k = deque.pop()
                temp.append(k.val)
                if times % 2:
                    if k.left: out.append(k.left)
                    if k.right: out.append(k.right)
                else:
                    if k.right: out.append(k.right)
                    if k.left: out.append(k.left)
                    # if k.right: out.append(k.right)
            res.append(temp)
            deque = out
            times += 1
        return res
