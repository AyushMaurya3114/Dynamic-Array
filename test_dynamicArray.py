import pytest
from meralist import MeraList

@pytest.fixture
def sample_list():
    L = MeraList()
    L.append(100)
    L.append("hello")
    L.append(1400)
    return L

def test_append(sample_list):
    sample_list.append(3.14)
    assert sample_list[3] == 3.14
    assert len(sample_list) == 4

def test_pop(sample_list):
    sample_list.pop()
    assert len(sample_list) == 2
    assert sample_list.find(1400) == 'ValueError- not found'

def test_find(sample_list):
    assert sample_list.find("hello") == 1
    assert sample_list.find("bye") == 'ValueError- not found'

def test_insert(sample_list):
    sample_list.insert(1, "inserted")
    assert sample_list[1] == "inserted"
    assert len(sample_list) == 4

def test_insert_out_of_bounds(sample_list):
    # Inserting at index greater than size should append at the end
    sample_list.insert(10, "end")
    assert sample_list[len(sample_list)-1] == "end"
    # Length should increase by 1
    assert len(sample_list) == 4

def test_delete_item(sample_list):
    del sample_list[0]
    assert sample_list.find(100) == 'ValueError- not found'
    assert len(sample_list) == 2

def test_remove(sample_list):
    sample_list.remove("hello")
    assert sample_list.find("hello") == 'ValueError- not found'

def test_clear(sample_list):
    sample_list.clear()
    assert len(sample_list) == 0

def test_getitem_out_of_bounds(sample_list):
    assert sample_list[10] == 'Error- out of bound'
    assert sample_list[-1] == 'Error- out of bound'

def test_resize(sample_list):
    # Add enough elements to trigger resize
    for i in range(10):
        sample_list.append(i)
    assert len(sample_list) == 13  # original 3 + 10 new
