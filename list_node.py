class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    @staticmethod
    def of(array):
        if array is None:
            return None
        head = ListNode(array[len(array) - 1])
        if len(array) > 1:
            for i in range(len(array) - 1, -1, -1):
                head = ListNode(array[i], head)
        return head

    def __str__(self):
        current = self
        nodes = []
        while current:
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)