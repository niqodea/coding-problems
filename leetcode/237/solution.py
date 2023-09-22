class ListNode:
    def __init__(self, x: "ListNode"):
        self.val = x
        self.next: "ListNode" | None = None


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        next_node = node.next
        if next_node is None:
            raise ValueError("Node is last in the list!")

        node.val = next_node.val
        node.next = next_node.next


if __name__ == "__main__":
    pass  # Implementing tests for this is cumbersome
