# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        temp = result
        div_amount = 0
        while l1 or l2 or div_amount:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_val = (l1_val + l2_val + div_amount)%10
            div_amount = (l1_val + l2_val + div_amount)//10
            temp.next = ListNode(sum_val)
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


print(Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))
print('asd')