from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    """Class for tree node"""
    data: int
    left: Optional[Node]=None
    right: Optional[Node]=None


class Tree:
    """Class for binary tree"""
    _head: Optional[Node]
    _size: int

    def __init__(self):
        self._head, self._size = None, 0

    def insert(self, data: int) -> None:
        """Insertion to the tree.
           If the data is already in the tree, it won't be inserted twice"""
        if self._head is None:
            self._head = Node(data)
            self._size += 1
            return

        temp = self._head
        while temp:
            if data == temp.data:
                return
            if data > temp.data:
                if temp.right:
                    temp = temp.right
                    continue
                temp.right = Node(data)
                break
            if temp.left:
                temp = temp.left
                continue
            temp.left = Node(data)
            break

        self._size += 1
  
    @property
    def size(self):
        return self._size

    def find(self, data: int) -> bool:
        """Try to find if the input value exists.
           Returns true if the data is in the tree, false otherwise"""
        temp = self._head
        while temp:
            if temp.data == data:
                return True
            temp = temp.left if data < temp.data else temp.right
        return False

    @property
    def height(self) -> int:
        """Returns the tree's height"""     
        height = -1
        nodes_current_layer, nodes_next_layer = [self._head], []

        while any(nodes_current_layer):
            height += 1
            for node in nodes_current_layer:
                if node:
                    nodes_next_layer += [node.left, node.right]
            nodes_current_layer, nodes_next_layer = nodes_next_layer, []
        
        return height

    def get_node_height(self, node: Node, height: int=-1) -> int:
        """Returns specific's node height""" 
        if node:
            return max(self.get_node_height(node.left, height + 1), 
                       self.get_node_height(node.right, height + 1))
        return height

    @property
    def height_recursion(self) -> int:
        """Returns the tree height using recursion""" 
        return self.get_node_height(self._head)

    def inorder(self) -> list:
        """Returns list of ordered vals"""  
        ordered = []
        stack = []
        current = self._head
        go_left_flag = 1
        
        while current:
            if go_left_flag and current.left:
                stack.append(current)
                current = current.left
                continue
            ordered.append(current.data)
            try:
                current, go_left_flag = \
                    (current.right, 1) if current.right else (stack.pop(), 0)
            except IndexError:
                break

        return ordered

    def get_node_inorder(self, node: Node, result: list) -> list:
        """Returns specific node height""" 
        if node:
            self.get_node_inorder(node.left, result)
            result.append(node.data)
            self.get_node_inorder(node.right, result)
        return result

    def inorder_recursion(self) -> list:
        """Returns list of ordered vals using recursion"""  
        return self.get_node_inorder(self._head, [])













