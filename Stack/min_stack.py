from typing import Any, List

from stack import Stack


class MinStack(Stack):

    @property
    def size(self) -> int:
        """Returnning the size of the stuck"""

        return int(len(self._items)/2)

    @property
    @Stack._get_item_decorator
    def min(self) -> int:
        """Returnning the min item or empty stack message"""

        return self._items[-2]

    @Stack._get_item_decorator
    def pop(self) -> Any:
        """Returnning the last item or empty stack message"""

        item = self._items.pop()
        self._items.pop()
        return item

    def push(self, item: Any) -> None:
        """Getting an item and appending the new min and new item to the end.
        Returnning none."""

        if not self.size or item < self.min:
            self._items.append(item)
        else:
            self._items.append(self.min)
        self._items.append(item)


if __name__=='__main__':

    print('init stack')
    stack = MinStack()
    print(f'empty: {stack.is_empty()}')
    print(f'size: {len(stack)}')
    print('--------------------------')
    print('push 6')
    stack.push(6)
    print(f'size: {len(stack)}')
    print(f'peek: {stack.peek()}')
    print(f'empty: {stack.is_empty()}')
    print(f'min: {stack.min}')
    print('--------------------------')
    print('push 7')
    stack.push(7)
    print(f'size: {len(stack)}')
    print(f'peek: {stack.peek()}')
    print(f'empty: {stack.is_empty()}')
    print(f'min: {stack.min}')
    print('--------------------------')
    print('push 5')
    stack.push(5)
    print(f'size: {len(stack)}')
    print(f'peek: {stack.peek()}')
    print(f'empty: {stack.is_empty()}')
    print(f'min: {stack.min}')
    print('--------------------------')
    print(f'pop {stack.pop()}')
    print(f'empty: {stack.is_empty()}')
    print(f'size: {len(stack)}')
    print(f'min: {stack.min}')
    print('--------------------------')
    print(f'pop {stack.pop()}')
    print(f'empty: {stack.is_empty()}')
    print(f'size: {len(stack)}')
    print(f'peek: {stack.peek()}')
    print(f'min: {stack.min}')
    print('--------------------------')
    print(f'pop {stack.pop()}')
    print(f'empty: {stack.is_empty()}')
    print(f'size: {len(stack)}')
    print(f'peek: {stack.peek()}')
    print(f'min: {stack.min}')
    print('--------------------------')
    print(f'pop {stack.pop()}')
    print(f'empty: {stack.is_empty()}')
    print(f'size: {len(stack)}')
    print(f'peek: {stack.peek()}')
    print(f'min: {stack.min}')
