#Reverse a singly linked list. 
#
# Example: 
#
# 
#Input: 1->2->3->4->5->NULL
#Output: 5->4->3->2->1->NULL
# 
#
# Follow up: 
#
# A linked list can be reversed either iteratively or recursively. Could you implement both? 
# Related Topics Linked List



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        pre = head
        cur = head.next
        head.next = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
        
#leetcode submit region end(Prohibit modification and deletion)
