'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]

限制：
0 <= 链表长度 <= 10000
'''

#答：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ## 递归
        # return self.reversePrint(head.next) + [head.val] if head else []
        
        ## 辅助栈
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
