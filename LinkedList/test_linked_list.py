import pytest
from linked_list import LinkedList


@pytest.fixture
def linked_list():
    new_list = LinkedList()
    new_list.add_last('Noa')
    new_list.add_last('Matan')
    new_list.add_last('Yaron')
    yield new_list
    del new_list


@pytest.fixture
def empty_list():
    empty_list = LinkedList()
    yield empty_list
    del empty_list


def test_size_len(linked_list):
    assert linked_list.size == len(linked_list) == 3
    linked_list.add_first('Koral')
    assert linked_list.size == len(linked_list) == 4
    linked_list.add_last('Liron')
    assert linked_list.size == len(linked_list) == 5
    linked_list.remove('Koral')
    assert linked_list.size == len(linked_list) == 4
    linked_list.remove('Koral')
    assert linked_list.size == len(linked_list) == 4


def test_remove(linked_list):
    assert linked_list.size == 3
    assert repr(linked_list) == 'LinkedList(Noa->Matan->Yaron)'
    linked_list.remove('Matan')
    assert repr(linked_list) == 'LinkedList(Noa->Yaron)'
    assert linked_list.size == 2


def test_is_empty(linked_list, empty_list):
    assert linked_list.is_empty() == False
    assert empty_list.is_empty() == True
    linked_list.remove('Matan')
    assert linked_list.is_empty() == False
    linked_list.remove('Noa')
    linked_list.remove('Yaron')
    assert linked_list.is_empty() == True


def test_iter(linked_list, empty_list):
    iter_empty = iter(empty_list)
    with pytest.raises(StopIteration):
        next(iter_empty)
    iter_not_empty = iter(linked_list)
    assert next(iter_not_empty) == 'Noa'
    assert next(iter_not_empty) == 'Matan'
    assert next(iter_not_empty) == 'Yaron'
    with pytest.raises(StopIteration):
        next(iter_not_empty)
