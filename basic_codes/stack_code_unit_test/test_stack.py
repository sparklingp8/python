import pytest
from stack import Stack
import time

# to run first do pip install pytest
# pytest -v
#

@pytest.fixture
def stack_object():
    return Stack(maxsize=10)


def test_should_create_stack_of_given_size(stack_object):
    assert stack_object is not None, "Stack object not created properly"


def test_should_return_maxsize(stack_object):
    assert stack_object.maxsize == 10, "Stack size improper"


def test_should_return_number_of_elements_in_stack(stack_object):
    assert stack_object.currentSize() == 0, "couldn't compute stack size"


def test_should_push_data(stack_object):
    stack_object.push(10)
    assert stack_object.currentSize() == 1, "stack not updated properly"


def test_should_return_list_elements(stack_object):
    stack_object.push(10)
    assert stack_object.elements() == [10], "stack is not updated properly"


def test_should_pop_top_element(stack_object):
    stack_object.push(10)
    assert stack_object.pop() == 10, "pop was not correct"


def test_should_return_none_on_pop_of_empty_list(stack_object):
    assert stack_object.pop() is None, "pop error in empty list"


def test_should_return_top_element_of_stack(stack_object):
    assert stack_object.peek() is None
