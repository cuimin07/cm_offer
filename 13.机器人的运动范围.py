'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 1：
输入：m = 3, n = 1, k = 0
输出：1

提示：
1 <= n,m <= 100
0 <= k <= 20
'''

#答：
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 深度优先搜索（dfs）
        def sum_ij(i,j):  # 定义和函数
            tmp = 0
            while i > 0:
                tmp += i % 10
                i //= 10
            while j > 0:
                tmp += j % 10
                j //= 10
            return tmp 
        def dfs(i, j):
            nonlocal res
            if (i, j) in marked \
                    or i == m \
                    or j == n \
                    or sum_ij(i, j) > k:
                return 
            marked.add((i, j))
            res += 1
            dfs(i+1, j), dfs(i, j+1)
                
        marked = set()
        res = 0
        dfs(0, 0)
        return res
