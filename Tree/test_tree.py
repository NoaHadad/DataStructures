import pytest
from tree import Tree


@pytest.fixture
def empty_tree():
    tree_example = Tree()
    yield tree_example
    del tree_example


@pytest.fixture
def root_tree():
    tree_example = Tree()
    tree_example.insert(5)
    yield tree_example
    del tree_example


@pytest.fixture
def tree():
    tree_example = Tree()
    tree_example.insert(5)
    tree_example.insert(93)
    tree_example.insert(72)
    tree_example.insert(24)
    tree_example.insert(76)
    tree_example.insert(108)
    tree_example.insert(51)
    yield tree_example
    del tree_example


def test_size(empty_tree, root_tree, tree):
    assert empty_tree.size == 0
    assert root_tree.size == 1   
    assert tree.size == 7
    tree.insert(10)
    assert tree.size == 8


def test_find(empty_tree, root_tree, tree):
    assert empty_tree.find(72) == False
    assert root_tree.find(72) == False
    assert tree.find(72) == True
    assert tree.find(8) == False


def test_height(empty_tree, root_tree, tree):
    assert empty_tree.height_recursion == empty_tree.height == -1
    assert root_tree.height_recursion == root_tree.height == 0
    assert tree.height_recursion == tree.height == 4
    tree.insert(10)
    assert tree.height_recursion == tree.height == 4
    tree.insert(8)
    assert tree.height_recursion == tree.height == 5    
    tree.insert(1)
    assert tree.height_recursion == tree.height == 5      


def test_inorder(empty_tree, root_tree, tree):
    assert empty_tree.inorder_recursion() == empty_tree.inorder() == []  
    assert root_tree.inorder_recursion() == root_tree.inorder() == [5]  
    assert tree.inorder_recursion() == tree.inorder() == [5, 24, 51, 72, 76, 93, 108]  