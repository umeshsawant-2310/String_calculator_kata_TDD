import string_calculator
import pytest


def test_string_calculator_string():
    result = string_calculator.calculator("")
    assert result == 0


def test_string_calculator_one_numbers():
    result = string_calculator.calculator("1")
    assert result == 1


def test_string_calculator_two_numbers():
    result = string_calculator.calculator("2,3")
    assert result == 5


def test_string_calculator_multi_numbers():
    result = string_calculator.calculator("1,2,3,4,5,6,7,8,9")
    assert result == 45


def test_string_calculator_including_alphabet():
    result = string_calculator.calculator("1,2,a,z,5")
    assert result == 35


def test_string_calculator_greater_1000_numbers():
    result = string_calculator.calculator("1546,1,2,3,4,1020,5,1030")
    assert result == 15


def test_negative_numbers_exception():
    with pytest.raises(Exception, match=r'negatives not allowed \[-1, -2, -3\]'):
        string_calculator.calculator('-1, -2, -3, 1, 2, 3')


def test_new_line():
    assert string_calculator.calculator('1\n2,3') == 6


def test_support_different_delimiters():
    assert string_calculator.calculator('//;\n1;2') == 3


def test_final():
    assert string_calculator.calculator('//[***]\n1***2***3') == 6
