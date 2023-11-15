from __future__ import annotations


class Node:
    def __init__(self, value: int = 0, next: Node | None = None):
        self.value = value
        self.next = next


class EmptyLinkedListError(Exception):
    ...


class NodeNotFoundError(Exception):
    ...


class OutOfBoundsError(Exception):
    ...


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def append(self, node: Node) -> None:
        if self.head is None:
            self.head = node
        else:
            current: Node = self.head
            while current.next:
                current = current.next
            current.next = node

    def prepend(self, node: Node) -> None:
        node.next = self.head
        self.head = node

    def find(self, value: int) -> Node | None:
        current: Node | None = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def to_list(self) -> list[int]:
        result: list[int] = []
        current: Node | None = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def delete(self, value: int) -> None:
        if self.head is None:
            raise EmptyLinkedListError("Cannot delete: empty list")

        if self.head.value == value:
            self.head = self.head.next
            return

        current: Node = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

        raise NodeNotFoundError(
            f"Cannot delete: node with value {value} not found"
        )

    def insert(self, node: Node, position: int) -> None:
        size: int = len(self.to_list())
        if not (-size - 1 <= position <= size):
            raise OutOfBoundsError(
                f"Position {position} out of bounds. List size: {size}"
            )

        if position == 0 or position == -size - 1:
            node.next = self.head
            self.head = node
            return

        if position < 0:
            position = size + position + 1

        current: Node = self.head                   # type: ignore
        for _ in range(position - 1):
            current = current.next                  # type: ignore
        node.next = current.next
        current.next = node

    def reverse(self) -> None:
        current: Node | None = self.head
        previous: Node | None = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def remove_duplicates(self) -> None:
        current: Node | None = self.head
        previous: Node | None = None
        values_seen: set[int] = set()
        while current:
            if current.value in values_seen:
                previous.next = current.next        # type: ignore
            else:
                previous = current
                values_seen.add(current.value)
            current = current.next


class AddTwoNumbers:
    """
    This class implements solution for the following problem:

    You are given two non-empty linked lists representing
    two non-negative integers. The digits are stored in reverse
    order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero,
    except the number 0 itself.

    (https://leetcode.com/problems/add-two-numbers/)
    """

    def solve(self, head_1: Node | None, head_2: Node | None) -> LinkedList:
        carry_flag: int = 0
        result: Node = Node()
        head: Node = result
        if head_1 is None or head_2 is None:
            raise EmptyLinkedListError("Cannot add: empty list(s)")
        current_node_1: Node | None = head_1
        current_node_2: Node | None = head_2
        while current_node_1 is not None or current_node_2 is not None:
            if current_node_1 is None:
                value_1 = 0
            else:
                value_1 = current_node_1.value
                current_node_1 = current_node_1.next

            if current_node_2 is None:
                value_2 = 0
            else:
                value_2 = current_node_2.value
                current_node_2 = current_node_2.next

            result.value = value_1 + value_2 + carry_flag
            carry_flag = 0
            if result.value > 9:
                result.value %= 10
                carry_flag = 1

            if current_node_1 or current_node_2:
                result.next = Node()
                result = result.next

        if carry_flag == 1:
            result.next = Node(1)

        result_list = LinkedList()
        result_list.head = head
        return result_list


class RemoveNthFromEnd:
    """
    This class implements solution for the following problem:

    Given the head of a linked list, remove the nth node from
    the end of the list and return its head.

    (https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
    """

    def solve(self, head: Node | None, n: int) -> Node | None:
        if head is None:
            raise EmptyLinkedListError("Cannot remove: empty list")
        if n <= 0:
            raise OutOfBoundsError("Only positive position values are allowed")
        right_pointer: Node = head
        left_pointer: Node = head
        previous: Node = Node(next=head)
        for i in range(n - 1):
            if not right_pointer.next:
                raise OutOfBoundsError(
                    f"Position {i + 2} out of bounds of linked list"
                )
            right_pointer = right_pointer.next
        while right_pointer.next is not None:
            previous = left_pointer
            left_pointer = left_pointer.next        # type: ignore
            right_pointer = right_pointer.next
        if left_pointer == head:
            head = left_pointer.next
        previous.next = left_pointer.next
        return head
