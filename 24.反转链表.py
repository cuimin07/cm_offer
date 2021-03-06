'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

限制：
0 <= 节点个数 <= 5000
'''

#答：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import deque
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代
        if not head: return None
        deq = deque()
        while head.next:
            deq.append(head)
            head = head.next
        temp = head
        while deq:
            node = deq.pop()
            node.next = temp.next
            temp.next = node
            temp = node
        return head
        
        # 双指针
        if not head: return None
        pre = head
        cur = None
        while pre:
            temp = ListNode(pre.val)
            temp.next = cur
            cur = temp
            pre = pre.next
        return cur
