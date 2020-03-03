'''
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

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
  [9,20],
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
        # 递归
        levels = []
        if not root: return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left: helper(node.left, level + 1)
            if node.right: helper(node.right, level + 1)
        
        helper(root, 0)
        return levels

        # 迭代
        from collections import deque
        levels = []
        if not root: return levels

        level = 0
        queue = deque([root, ])
        while queue:
            levels.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level += 1
        return levels
