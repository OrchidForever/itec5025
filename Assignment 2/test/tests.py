'''
Written by Github Copilot
Edited and new tests added by Kai

It includes tests for arithmetic operations, comparison operations, and logical operations.
'''

import pytest
import sys
import os
from io import StringIO

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import calculate
# Fix the import names to match your actual function names
from faker import process_arithmetic, print_greeting, print_exit, print_error_processing, print_help

# Test cases for the calculate function from utils.py
class TestCalculateFunction:
    """Test cases for the calculate function from utils.py"""
    
    def test_addition(self):
        """Test arithmetic addition operations"""
        assert calculate(5, 3, '+') == 8
        assert calculate(-2, 7, '+') == 5
        assert calculate(0, 0, '+') == 0
        assert calculate(3.5, 2.5, '+') == 6.0
    
    def test_subtraction(self):
        """Test arithmetic subtraction operations"""
        assert calculate(10, 3, '-') == 7
        assert calculate(-5, -2, '-') == -3
        assert calculate(0, 5, '-') == -5
        assert calculate(7.5, 2.5, '-') == 5.0
    
    def test_multiplication(self):
        """Test arithmetic multiplication operations"""
        assert calculate(4, 3, '*') == 12
        assert calculate(-2, 5, '*') == -10
        assert calculate(0, 100, '*') == 0
        assert calculate(2.5, 4, '*') == 10.0
    
    def test_division(self):
        """Test arithmetic division operations"""
        assert calculate(12, 3, '/') == 4
        assert calculate(10, 4, '/') == 2.5
        assert calculate(-8, 2, '/') == -4
    
    def test_division_by_zero(self):
        """Test division by zero handling"""
        result = calculate(10, 0, '/')
        assert result == "You silly goose. You can't divide by zero!"
    
    def test_equality_comparison(self):
        """Test equality comparison operations"""
        assert calculate(5, 5, '=') == True
        assert calculate(5, 3, '=') == False
        assert calculate(-1, -1, '=') == True
        assert calculate(0, 1, '=') == False
    
    def test_greater_than_comparison(self):
        """Test greater than comparison operations"""
        assert calculate(5, 3, '>') == True
        assert calculate(3, 5, '>') == False
        assert calculate(5, 5, '>') == False
        assert calculate(0, -1, '>') == True
    
    def test_less_than_comparison(self):
        """Test less than comparison operations"""
        assert calculate(3, 5, '<') == True
        assert calculate(5, 3, '<') == False
        assert calculate(5, 5, '<') == False
        assert calculate(-1, 0, '<') == True
    
    def test_greater_than_or_equal_comparison(self):
        """Test greater than or equal comparison operations"""
        assert calculate(5, 3, '>=') == True
        assert calculate(5, 5, '>=') == True
        assert calculate(3, 5, '>=') == False
    
    def test_less_than_or_equal_comparison(self):
        """Test less than or equal comparison operations"""
        assert calculate(3, 5, '<=') == True
        assert calculate(5, 5, '<=') == True
        assert calculate(5, 3, '<=') == False
    
    def test_not_equal_comparison(self):
        """Test not equal comparison operations"""
        assert calculate(5, 3, '!=') == True
        assert calculate(5, 5, '!=') == False
        assert calculate(-1, 10, '!=') == True

class TestProcessArithmetic:
    """Test cases for the process_arithmetic function from faker.py"""
    
    def test_basic_addition(self, capsys):
        """Test basic addition with symbols"""
        result = process_arithmetic("5 + 3")    
        assert result == 8.0
    
    def test_basic_subtraction(self, capsys):
        """Test basic subtraction with symbols"""
        result = process_arithmetic("10 - 4")
        assert result == 6.0
    
    def test_basic_multiplication(self, capsys):
        """Test basic multiplication with symbols"""
        result = process_arithmetic("6 * 7")
        assert result == 42.0
    
    def test_basic_division(self, capsys):
        """Test basic division with symbols"""
        result = process_arithmetic("15 / 3")
        assert result == 5.0
    
    def test_comparison_operations(self, capsys):
        """Test comparison operations"""
        assert process_arithmetic("5 = 5") == True
        assert process_arithmetic("5 > 3") == True
        assert process_arithmetic("3 < 5") == True
    
    def test_compound_expressions(self, capsys):
        """Test expressions like '10/4' as one word"""
        result = process_arithmetic("10/4")
        assert result == 2.5
    
    def test_punctuation_handling(self, capsys):
        """Test that punctuation is handled correctly"""
        assert process_arithmetic("5+3?") == 8
        assert process_arithmetic("10!=4") == True
        assert process_arithmetic("6 != 7.") == True
        assert process_arithmetic("6*7.") == 42

    def test_invalid_input(self, capsys):
        """Test invalid inputs that should return False"""
        assert process_arithmetic("hello world") == None
        assert process_arithmetic("5") == None  # Only one number
        assert process_arithmetic("plus minus") == None  # No numbers
        assert process_arithmetic("") == None  # Empty string

class TestPrintFunctions:
    """Test cases for print functions from faker.py"""
    
    def test_print_greeting(self, capsys):
        """Test that greeting prints expected content"""
        print_greeting()
        captured = capsys.readouterr()
        assert "Hello!" in captured.out
        assert "silly goose" in captured.out
    
    def test_print_exit(self, capsys):
        """Test that exit message prints expected content"""
        print_exit()
        captured = capsys.readouterr()
        assert "Thank you" in captured.out
        assert "Goodbye" in captured.out
    
    def test_print_error_processing(self, capsys):
        """Test that error message prints expected content"""
        print_error_processing()
        captured = capsys.readouterr()
        assert "Yikes" in captured.out
        assert "didn't understand" in captured.out
    
    def test_print_help(self, capsys):
        """Test that help message prints expected content"""
        print_help()
        captured = capsys.readouterr()
        assert "examples" in captured.out
        assert "5 + 6" in captured.out

# Parametrized tests for more comprehensive coverage
@pytest.mark.parametrize("num1,num2,op,expected", [
    (5, 3, '+', 8),
    (10, 4, '-', 6),
    (6, 7, '*', 42),
    (15, 3, '/', 5),
    (5, 5, '=', True),
    (5, 3, '>', True),
    (3, 5, '<', True),
    (5, 5, '>=', True),
    (3, 5, '<=', True),
    (5, 3, '!=', True),
])
def test_calculate_parametrized(num1, num2, op, expected):
    """Parametrized test for calculate function"""
    assert calculate(num1, num2, op) == expected

# Only test operations that your current process_arithmetic function can handle
@pytest.mark.parametrize("input_str,expected", [
    ("5 + 3", 8),
    ("5+3", 8),
    ("10 - 4", 6),
    ("6 * 7", 42),
    ("15 / 3", 5),
    ("5 = 5", True),
    ("5 > 3", True),
    ("3 < 5", True),
    ("5 >= 5", True),
    ("3 <= 5", True),
    ("5 != 3", True),
    ("5!=3", True),
    ("hello world", None),
    ("", None),
    ("5", None),
])
def test_process_arithmetic_parametrized(input_str, expected, capsys):
    """Parametrized test for process_arithmetic function"""
    assert process_arithmetic(input_str) == expected

# Simplified fixtures - only test what your current code can handle
@pytest.fixture
def basic_arithmetic_test_cases():
    """Fixture providing test cases for basic arithmetic operations"""
    return [
        ("5 + 3", 8),
        ("10 - 4", 6),
        ("6 * 7", 42),
        ("15 / 3", 5),
        ("5+3", 8),
        ("10-4", 6),
        ("6*7", 42),
        ("15/3", 5),
    ]

@pytest.fixture
def comparison_test_cases():
    """Fixture providing test cases for comparison operations"""
    return [
        ("5 = 5", True),
        ("5 > 3", True),
        ("3 < 5", True),
        ("5 >= 5", True),
        ("3 <= 5", True),
        ("5 != 3", True),
        ("5=5", True),
        ("5>3", True),
        ("3<5", True),
        ("5>=5", True),
        ("3<=5", True),
        ("5!=3", True),
    ]

def test_arithmetic_with_fixture(basic_arithmetic_test_cases, capsys):
    """Test arithmetic operations using fixture data"""
    for input_str, expected in basic_arithmetic_test_cases:
        result = process_arithmetic(input_str)
        assert result == expected

def test_comparison_with_fixture(comparison_test_cases, capsys):
    """Test comparison operations using fixture data"""
    for input_str, expected in comparison_test_cases:
        result = process_arithmetic(input_str)
        assert result == expected