from src.homework.main import (
    Node,
    LinkedList,
    EmptyLinkedListError,
    NodeNotFoundError,
    OutOfBoundsError,
    AddTwoNumbers,
    RemoveNthFromEnd,
)
import pytest


class TestLinkedList:
    def test_create_node(self) -> None:
        node_0: Node = Node()
        assert node_0.value == 0
        assert node_0.next is None

        node_1: Node = Node(100)
        assert node_1 is not None

        node_2: Node = Node(200, node_1)
        assert node_2 is not None
        assert node_2.value == 200
        assert node_2.next is node_1

        assert node_2.next.next is None

    def test_create_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        assert linked_list is not None
        assert linked_list.head is None

    def test_append(self) -> None:
        linked_list: LinkedList = LinkedList()
        node_1: Node = Node(100)
        linked_list.append(node_1)
        assert linked_list.head is node_1

        node_2: Node = Node(200)
        linked_list.append(node_2)
        assert linked_list.head.next is node_2

    def test_prepend(self) -> None:
        linked_list: LinkedList = LinkedList()
        node_1: Node = Node(100)
        linked_list.prepend(node_1)
        assert linked_list.head is node_1

        node_2: Node = Node(200)
        linked_list.prepend(node_2)
        assert linked_list.head is node_2

    def test_find(self) -> None:
        linked_list: LinkedList = LinkedList()
        assert linked_list.find(100) is None
        node_1: Node = Node(100)
        node_2: Node = Node(200)
        node_3: Node = Node(300)
        node_4: Node = Node(300)
        node_5: Node = Node(400)
        linked_list.append(node_1)
        linked_list.append(node_2)
        linked_list.append(node_3)
        linked_list.append(node_4)
        linked_list.append(node_5)

        assert linked_list.find(100) is node_1
        assert linked_list.find(300) is node_3
        assert linked_list.find(400) is node_5
        assert linked_list.find(500) is None

    def test_to_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        assert linked_list.to_list() == []
        linked_list.append(Node(100))
        assert linked_list.to_list() == [100]
        linked_list.append(Node(200))
        assert linked_list.to_list() == [100, 200]

    def test_delete(self) -> None:
        linked_list: LinkedList = LinkedList()
        with pytest.raises(EmptyLinkedListError) as exc:
            linked_list.delete(100)
        assert str(exc.value) == "Cannot delete: empty list"

        linked_list.append(Node(100))
        linked_list.append(Node(200))
        linked_list.append(Node(300))

        linked_list.delete(100)
        assert linked_list.to_list() == [200, 300]

        linked_list.delete(300)
        assert linked_list.to_list() == [200]

        with pytest.raises(NodeNotFoundError) as exc:       # type: ignore
            linked_list.delete(300)
        assert str(exc.value) == "Cannot delete: node with value 300 not found"

        linked_list.delete(200)
        assert linked_list.to_list() == []

    def test_insert(self) -> None:
        linked_list: LinkedList = LinkedList()
        node_1: Node = Node(100)
        linked_list.insert(node_1, 0)
        assert linked_list.head is node_1

        node_2: Node = Node(200)
        linked_list.insert(node_2, 0)
        assert linked_list.head is node_2

        node_3: Node = Node(300)
        linked_list.insert(node_3, 2)
        assert linked_list.head.next.next is node_3         # type: ignore

        with pytest.raises(OutOfBoundsError) as exc:
            linked_list.insert(Node(1000), 10)
        assert str(exc.value) == "Position 10 out of bounds. List size: 3"

        node_4: Node = Node(400)
        linked_list.insert(node_4, -1)
        assert linked_list.head.next.next.next is node_4    # type: ignore

        node_5: Node = Node(500)
        linked_list.insert(node_5, -4)
        assert linked_list.head.next is node_5

        node_6: Node = Node(600)
        linked_list.insert(node_6, -6)
        assert linked_list.head is node_6

        with pytest.raises(OutOfBoundsError) as exc:
            linked_list.insert(Node(1000), -10)
        assert str(exc.value) == "Position -10 out of bounds. List size: 6"

    def test_reverse(self) -> None:
        linked_list: LinkedList = LinkedList()
        linked_list.reverse()
        assert linked_list.to_list() == []

        linked_list.append(Node(100))
        linked_list.reverse()
        assert linked_list.to_list() == [100]

        linked_list.append(Node(200))
        linked_list.append(Node(300))
        linked_list.reverse()
        assert linked_list.to_list() == [300, 200, 100]

    def test_remove_duplicates(self) -> None:
        linked_list: LinkedList = LinkedList()
        linked_list.remove_duplicates()
        assert linked_list.to_list() == []

        linked_list.append(Node(100))
        linked_list.remove_duplicates()
        assert linked_list.to_list() == [100]

        linked_list.append(Node(100))
        linked_list.remove_duplicates()
        assert linked_list.to_list() == [100]

        linked_list.append(Node(200))
        linked_list.append(Node(300))
        linked_list.remove_duplicates()
        assert linked_list.to_list() == [100, 200, 300]

        linked_list.append(Node(300))
        linked_list.remove_duplicates()
        assert linked_list.to_list() == [100, 200, 300]

        linked_list.append(Node(300))
        linked_list.append(Node(300))
        linked_list.append(Node(400))
        linked_list.append(Node(400))
        linked_list.append(Node(200))
        linked_list.append(Node(500))
        linked_list.append(Node(200))
        linked_list.append(Node(600))
        linked_list.remove_duplicates()
        assert linked_list.to_list() == [100, 200, 300, 400, 500, 600]


class TestAddTwoNumbers:
    def test_solve(self) -> None:
        add: AddTwoNumbers = AddTwoNumbers()
        linked_list_1: LinkedList = LinkedList()
        linked_list_2: LinkedList = LinkedList()
        linked_list_1.append(Node(1))
        with pytest.raises(EmptyLinkedListError) as exc:
            add.solve(linked_list_1.head, linked_list_2.head)
        assert str(exc.value) == "Cannot add: empty list(s)"

        linked_list_2.append(Node(1))
        result: LinkedList = add.solve(linked_list_1.head, linked_list_2.head)
        assert int("".join(map(str, result.to_list()))) == 2

        linked_list_1.prepend(Node(6))
        linked_list_2.prepend(Node(7))
        result = add.solve(linked_list_1.head, linked_list_2.head)
        assert int("".join(map(str, result.to_list()))) == 33

        linked_list_1.prepend(Node(4))
        result = add.solve(linked_list_1.head, linked_list_2.head)
        assert int("".join(map(str, result.to_list()))) == 181

        linked_list_1.append(Node(9))
        linked_list_2.append(Node(9))
        result = add.solve(linked_list_1.head, linked_list_2.head)
        assert int("".join(map(str, result.to_list()))) == 18001


class TestRemoveNthFromEnd:
    def test_solve(self) -> None:
        remove = RemoveNthFromEnd()
        linked_list: LinkedList = LinkedList()
        with pytest.raises(EmptyLinkedListError) as exc:
            remove.solve(linked_list.head, 1)
        assert str(exc.value) == "Cannot remove: empty list"
        linked_list.append(Node(100))
        linked_list.append(Node(200))
        linked_list.append(Node(300))
        linked_list.append(Node(400))

        with pytest.raises(OutOfBoundsError) as exc:        # type: ignore
            remove.solve(linked_list.head, -1)
        assert str(exc.value) == "Only positive position values are allowed"

        with pytest.raises(OutOfBoundsError) as exc:        # type: ignore
            remove.solve(linked_list.head, 5)
        assert str(exc.value) == "Position 5 out of bounds of linked list"

        linked_list.head = remove.solve(linked_list.head, 4)
        assert linked_list.to_list() == [200, 300, 400]

        linked_list.head = remove.solve(linked_list.head, 2)
        assert linked_list.to_list() == [200, 400]

        linked_list.head = remove.solve(linked_list.head, 1)
        assert linked_list.to_list() == [200]

        linked_list.head = remove.solve(linked_list.head, 1)
        assert linked_list.to_list() == []
