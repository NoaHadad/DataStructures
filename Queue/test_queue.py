import pytest
from queue import Queue
from queue_exceptions import EmptyQueueException


@pytest.fixture
def not_empty_queue():
    q = Queue([1,2,3,4,5])
    yield q
    del q


@pytest.fixture
def empty_queue():
    q = Queue()
    yield q
    del q


def test_init_queue(not_empty_queue, empty_queue):

    assert not_empty_queue.peek() == 1
    assert not_empty_queue.size == 5
    assert not_empty_queue.capacity == 5

    with pytest.raises(EmptyQueueException):
        empty_queue.peek()
    assert empty_queue.size == 0
    assert empty_queue.capacity == 10


def test_enqueue(not_empty_queue, empty_queue):

    not_empty_queue.enqueue(6)
    assert not_empty_queue._items[5] == 6
    assert not_empty_queue.size == 6
    assert not_empty_queue.capacity == 10

    empty_queue.enqueue(6)
    assert empty_queue._items[0] == 6
    assert empty_queue.size == 1
    assert not_empty_queue.capacity == 10


def test_dequeue(not_empty_queue, empty_queue):

    assert not_empty_queue.dequeue() == 1
    assert not_empty_queue.dequeue() == 2
    assert not_empty_queue.dequeue() == 3
    assert not_empty_queue.dequeue() == 4
    assert not_empty_queue.dequeue() == 5
    with pytest.raises(EmptyQueueException):
        not_empty_queue.dequeue()

    with pytest.raises(EmptyQueueException):
        empty_queue.dequeue()


def test_peek(not_empty_queue, empty_queue):

    with pytest.raises(EmptyQueueException):
        empty_queue.peek()

    assert not_empty_queue.peek() == 1
    not_empty_queue.enqueue(6)
    assert not_empty_queue.peek() == 1
    not_empty_queue.dequeue()
    assert not_empty_queue.peek() == 2


def test_capcity_size_resize(not_empty_queue):

    assert not_empty_queue.size == 5
    assert not_empty_queue.capacity == 5
    assert not_empty_queue._first_index == 0

    not_empty_queue.dequeue()
    assert not_empty_queue.size == 4
    assert not_empty_queue.capacity == 5
    assert not_empty_queue._first_index == 1

    not_empty_queue.dequeue()
    assert not_empty_queue.size == 3
    assert not_empty_queue.capacity == 5
    assert not_empty_queue._first_index == 2

    not_empty_queue.enqueue(6)
    assert not_empty_queue.size == 4
    assert not_empty_queue.capacity == 5
    assert not_empty_queue._first_index == 2

    not_empty_queue.enqueue(7)
    assert not_empty_queue.size == 5
    assert not_empty_queue.capacity == 5
    assert not_empty_queue._first_index == 2

    # resize
    not_empty_queue.enqueue(8)
    assert not_empty_queue.size == 6
    assert not_empty_queue.capacity == 10
    assert not_empty_queue._first_index == 0


def test_first_index(not_empty_queue):

    assert not_empty_queue._first_index == 0

    assert not_empty_queue.dequeue()
    assert not_empty_queue._first_index == 1

    not_empty_queue.enqueue(6)
    assert not_empty_queue._first_index == 1

    assert not_empty_queue.dequeue()
    assert not_empty_queue._first_index == 2

    assert not_empty_queue.dequeue()
    assert not_empty_queue._first_index == 3

    assert not_empty_queue.dequeue()
    assert not_empty_queue._first_index == 4

    assert not_empty_queue.dequeue()
    assert not_empty_queue._first_index == 0
