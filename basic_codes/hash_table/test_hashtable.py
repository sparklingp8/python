from hashtable import HashTable, BLANK
import pytest


@pytest.fixture
def hash_table():
    sample_data = HashTable(100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data


def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None


def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100, "Capacity is not assigning"


def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [BLANK, BLANK, BLANK], "empty slots not created correctly"


def test_should_insert_key_value_pairs(hash_table):
    assert "hello" in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values
    assert len(hash_table) == 100


def test_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["key"] = None
    assert None in hash_table.values


def test_should_raise_error_on_missing_key(hash_table):
    with pytest.raises(KeyError):  # as exception_info:
        var = hash_table["missing"]
    # assert exception_info.value.args[0] == "missing_key" #no longer needed


def test_should_find_key(hash_table):
    assert "hola" in hash_table


def test_should_get_value(hash_table):
    assert hash_table.get("hola") == "hello"


def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get("missing_key") is None


def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get("missing_key", "default") == "default"


def test_should_get_value_with_default(hash_table):
    assert hash_table.get("hola", "default") == "hello"


@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass


def test_should_always_pass():
    assert 2 + 2 == 4, "This is dummy test"
