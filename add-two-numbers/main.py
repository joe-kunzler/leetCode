# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))

    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode(0)
        curr = head
        print('here is curr:', curr)
        while l1 or l2 or carry:
            val = carry
            print('here is first val:', val)
            if l1:
                val += l1.val
                print('here is val 2', val)
                l1 = l1.next
                print('here is val 3', l1)
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            curr = curr.next
        print(head.__dict__)
        print(head.next.__dict__)
        print(head.next.next.__dict__)
        print(head.next.next.next.__dict__)
        return head.next.val
