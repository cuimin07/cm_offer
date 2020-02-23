'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2
输出：2

示例 2：
输入：n = 7
输出：21

提示：
0 <= n <= 100
'''

#答：
class Solution:
    def numWays(self, n: int) -> int:
        # 动态规划
        first, second = 1, 1
        for _ in range(n):
            first, second = second, first + second
        return first % 1000000007
