class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self.length = 0

    def __iter__(self):
        items = []
        curr = self._head

        while curr:
            items.append(curr.value())
            curr = curr._next()
        return iter(items)

    def __len__(self):
        return self.length

    def head(self):
        if not self.head:
            raise EmptyListException("empty")

    def push(self, value):
        node = Node(value)
        node._next = self.head
        self._head = node
        self.length +=1

    def pop(self):
        pass

    def reversed(self):
        pass


class EmptyListException(Exception):
    pass
