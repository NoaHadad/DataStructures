from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:

    data: str
    prev: Optional[Node] = None
    next: Optional[Node] = None


@dataclass(repr=False, eq=False)
class LinkedList:

    _head: Optional[Node] = None
    _tail: Optional[Node] = None
    _size: int = 0

    @property
    def size(self) -> int:
        return self._size

    def add_first(self, data: str) -> None:
        print(self._head) 
        if self._head is None:
            self._head = self._tail = Node(data)
        else:
            temp = self._head
            self._head = Node(data)
            self._head.next = temp
            temp.prev = self._head
        self._size += 1

    def add_last(self, data: str) -> None:
        if self._head is None:
            self._head = self._tail = Node(data)
        else:
            temp = self._tail
            self._tail = Node(data)
            self._tail.prev = temp
            temp.next = self._tail
        self._size += 1

    def search(self, data: str) -> bool:
        if self._head is None:
            return False
        temp = self._head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def remove(self, data: str) -> bool:
        if self._head is None:
            return False
        temp = self._head
        while temp:
            if temp.data == data:
                if temp == self._head:
                    if self._head == self._tail:
                         self._head = self._tail = None
                    else:
                         self._head = self._head.next
                         self._head.prev = None
                elif temp == self._tail:
                    self._tail = self._tail.prev
                    self._tail.next = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                del temp
                self._size -= 1
                return True
            temp = temp.next
        return False

    def reverse(self) -> None:
        if self._head is None:
            return
        temp = self._head
        while temp:
            next = temp.next
            temp.next = temp.prev
            temp.prev = next
            temp = next
        self._head, self._tail = self._tail, self._head

    def is_empty(self) -> bool:
        return not bool(self._head)

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> LinkedList:
        self._current = self._head
        return self

    def __next__(self) -> str:
        if self._current is not None:
            res = self._current.data
            self._current = self._current.next
            return res
        raise StopIteration

    def __eq__(self, other: LinkedList) -> bool:
        if len(self) != len(other):
            return False
        if not len(self):
            return True
        temp = self._head
        temp_other = other._head
        while temp:
            if temp.data != temp_other.data:
                return False
            temp = temp.next
            temp_other = temp_other.next
        return True

    def __repr__(self) -> str:
        if self._head is None:
            return 'EmptyLinkedList'
        list_repr = self._head.data
        temp = self._head.next
        while temp:
            list_repr += f'->{temp.data}'
            temp = temp.next
        return f'LinkedList({list_repr})'

