"""Tests"""


MY_DICT = {1: "first", 2: "second"}
SIMPLE_TURPLE = [3, 6, 1, 8]
MY_SET = {1, 4, 6, 7}
MY_SET2 = {2, 5, 8, 4}


def setup():
    """setup"""
    print("basic setup into module")


def teardown():
    """teardown"""
    print("basic teardown into module")


def setup_module():
    """setup_module"""
    print("Start my tests in module!")


def teardown_module():
    """teardown_module"""
    print("By, by from module!")


def test_numbers_5_2():
    """Test"""
    print("test1")
    print("5-2")
    assert 5 - 2 == 3


def test_len_list():
    """Test"""
    print("test2")
    print("len([1,3,5,7,9])")
    assert len([1, 3, 5, 7, 9]) == 5


def test_max_of_list():
    """Test"""
    print("test3")
    print("max_of_list")
    assert max([3, 6, 1, 9, 2]) == 9


def test_sum_two_strings():
    """Test"""
    print("test4")
    print("sum_two_strings")
    assert "Hello, " + "world!" == "Hello, world!"


def test_multiplication_string():
    """Test"""
    print("test5")
    print("multiplication string")
    assert "hello!" * 3 == "hello!""hello!""hello!"


def test_turple():
    """Test"""
    print("test6")
    print("turple")
    assert SIMPLE_TURPLE[2] == 1


def test_turple_2():
    """test_turlpe"""
    print("test7")
    print("turple2")
    assert len(SIMPLE_TURPLE) == 4


def test_dictionary():
    """Test"""
    print("test8")
    print("dictionary")
    assert MY_DICT[2] == "second"


def test_dictionary_two():
    """Test"""
    print("test9")
    print("dictionary2")
    assert 1 in MY_DICT


def test_sets():
    """Test"""
    print("test10")
    print("set")
    assert MY_SET.intersection(MY_SET2) == {4}
