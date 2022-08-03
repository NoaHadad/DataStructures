
from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class Stack:

    _items : list[Any] = field(default_factory = lambda : [])

    @property
    def size(self) -> int:
        """Returnning the size of the stuck"""

        return len(self._items)

    def __len__(self):
        """Returnning the length of the stuck"""

        return self.size

    def push(self, item: Any) -> None:
        """Getting an item and appending it to the end.
        Returnning none."""

        self._items.append(item)

    def _get_item_decorator(func):
        def wrapper(self):
            try:
                return func(self)
            except IndexError:
                return 'stack is empty'
        return wrapper

    @_get_item_decorator
    def pop(self) -> Any:
        """Returnning the last item or empty stack message"""
 
        return self._items.pop()

    @_get_item_decorator
    def peek(self) -> Any:
        """Returnning the last item or empty stack message"""

        return self._items[-1]

    def is_empty(self) -> bool:
        """Checking if the stuck is empty.
        Returning boolean val."""

        return self.size == 0


if __name__=='__main__':

    print('init stack')
    stack = Stack()
    print(f'empty: {stack.is_empty()}')
    print(f'size: {len(stack)}')
    print('--------------------------')
    print('push 6')
    stack.push(6)
    print(f'size: {len(stack)}')
    print(f'peek: {stack.peek()}')
    print(f'empty: {stack.is_empty()}')
    print('--------------------------')
    print('push 7')
    stack.push(7)
    print(f'size: {len(stack)}')
    print(f'peek: {stack.peek()}')
    print(f'empty: {stack.is_empty()}')
    print('--------------------------')
    print(f'pop {stack.pop()}')
    print(f'empty: {stack.is_empty()}')
    print(f'size: {len(stack)}')
    print('--------------------------')
    print(f'pop {stack.pop()}')
    print(f'empty: {stack.is_empty()}')
    print(f'size: {len(stack)}')
    print(f'peek: {stack.peek()}')
    print('--------------------------')
    print(f'pop: {stack.pop()}')
