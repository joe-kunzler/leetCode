# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        carry = 0
        head = ListNode(0)
        print(head)
        curr = head
        print(curr)
        while l1 or l2 or carry:
            val = carry
            print(val)
            if l1:
                val += l1.val
                print(val)
                l1 = l1.next
                print(l1)
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            curr = curr.next
        return head.next