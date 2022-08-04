from dataclasses import dataclass, field
from typing import List, Optional, Any

from queue_exceptions import EmptyQueueException


DEFAULT_CAPACITY = 10


@dataclass
class Queue:

    _items : Optional[List[Any]] = None
    _first_index : int = field(default=0, init=False)
    _size : int = field(init=False)
    _capacity : int = field(init=False)

    def __post_init__(self):
        if self._items is None:
            self._capacity : int = DEFAULT_CAPACITY
            self._items = [0]*DEFAULT_CAPACITY
            self._size = 0
        else:
            self._capacity = self._size = len(self._items)

    @property
    def size(self) -> int:
        return self._size

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def _insert_index(self) -> int:
        place = self._first_index + self._size
        if place >= self._capacity:
            return (place - self._capacity)
        return place

    def _resize(self) -> None:
        """increasing the size of the items' list by 2"""

        print('resizing')
        new_items = [0]*(self._capacity*2)
        new_index = 0

        for index in range(self._first_index, self._size):
            new_items[new_index] = self._items[index]
            new_index += 1

        for index in range(0, self._first_index):
            new_items[new_index] = self._items[index]
            new_index += 1

        del self._items
        self._items = new_items
        self._first_index = 0
        self._capacity *= 2

    def peek(self) -> Any:
        """returns the first item or raises EmptyQueueException"""

        if self._size:
            return self._items[self._first_index]
        else:
            raise EmptyQueueException

    def dequeue(self) -> Any:
        """returns the first item or raises EmptyQueueException.
        the item will be removed from the queue"""

        if self._size:
            first_item : Any = self._items[self._first_index]
            self._first_index = 0 if self._first_index == (self._capacity - 1) else (self._first_index + 1)
            self._size -= 1
            return first_item
        else:
            raise EmptyQueueException

    def enqueue(self, item: Any) -> None:
        """insert an item to the end of the queue"""

        if self._size == self._capacity:
            self._resize()

        self._items[self._insert_index] = item
        self._size += 1
