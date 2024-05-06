from list_node import ListNode


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def removeNodes(self, head: ListNode) -> ListNode:
        head = self.reverse(head)
        x = head.val
        tmp = ListNode(0)
        prev = tmp
        while head:
            while head and head.val < x:
                head = head.next
            if not head:
                tmp.next = None
                break
            x = head.val
            tmp.next = head
            tmp = tmp.next
            head = head.next
        return self.reverse(prev.next)


# print(Solution.removeNodes(None))
print(Solution().removeNodes(head=ListNode.of([5, 2, 13, 3, 8])))
