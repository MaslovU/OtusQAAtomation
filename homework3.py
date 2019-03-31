"""Tests"""


MY_DICT = {1: "first", 2: "second"}
SIMPLE_TUPLE = [3, 6, 1, 8]
MY_SET = {1, 4, 6, 7}
MY_SET2 = {2, 5, 8, 4}


def setup():
    """setup function"""
    print("basic setup into module")


def teardown():
    """teardown function"""
    print("basic teardown into module")


def setup_module():
    """setup_module"""
    print("Start my tests in module!")


def teardown_module():
    """teardown_module"""
    print("By, by from module!")


def test_numbers_5_2():
    """Test for numbers"""
    print("test1")
    print("5-2")
    assert 5 - 2 == 3


def test_len_list():
    """Test for check len list"""
    print("test2")
    print("len([1,3,5,7,9])")
    assert len([1, 3, 5, 7, 9]) == 5


def test_max_of_list():
    """Test for check max element in list"""
    print("test3")
    print("max_of_list")
    assert max([3, 6, 1, 9, 2]) == 9


def test_sum_two_strings():
    """Test for string"""
    print("test4")
    print("sum_two_strings")
    assert "Hello, " + "world!" == "Hello, world!"


def test_multiplication_string():
    """Test for check multiplication string"""
    print("test5")
    print("multiplication string")
    assert "hello!" * 3 == "hello!""hello!""hello!"


def test_tuple():
    """Test for  find element in tuple"""
    print("test6")
    print("tuple")
    assert SIMPLE_TUPLE[2] == 1


def test_tuple_2():
    """test_for check len of tuple"""
    print("test7")
    print("tuple2")
    assert len(SIMPLE_TUPLE) == 4


def test_dictionary():
    """Test for dictionary"""
    print("test8")
    print("dictionary")
    assert MY_DICT[2] == "second"


def test_dictionary_two():
    """Test for check find key in dictionary"""
    print("test9")
    print("dictionary2")
    assert 1 in MY_DICT


def test_sets():
    """Test for sets"""
    print("test10")
    print("set")
    assert MY_SET.intersection(MY_SET2) == {4}
