import pytest 
import random
from bubble_sort import bubble_sort


def test_bubble_sort_short_list():
    data = [ 2,3,1,]
    bubble_sort(data)
    assert data == [1,2,3]

def test_bubble_sort_long_list():
    list_size = 100

    data_to_sort = list(range(list_size))
    expected_data  =list(range(list_size))

    random.shuffle(data_to_sort)

    bubble_sort(data_to_sort)

    assert data_to_sort == expected_data
    


def test_bubble_sort_empty_list():
    data=[]
    bubble_sort(data)
    assert data == []


def test_bubble_sort_parameter_is_not_a_list():
    with pytest.raises(TypeError) as excinfo:
        bubble_sort(123)
    assert "Input must be a list" in str(excinfo.value)

    with pytest.raises(TypeError):
        bubble_sort("a string")

    
    with pytest.raises(TypeError):
        bubble_sort(None)

    with pytest.raises(TypeError):
        bubble_sort((1,2,3))

    with pytest.raises(TypeError):
        bubble_sort({"a": 1, "b": 2})

        