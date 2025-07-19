# This files was written by Github Copilot
# and edited by Brenna Auker.
# Changes include adding more test cases based on the testing I did and issues I ran into while developing.

import pytest
import sys
import os
from io import StringIO

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import calculate
from faker import processArithmetic, printGreeting, printExit, printErrorProcessing, printHelp

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
    """Test cases for the processArithmetic function from faker.py"""
    
    def test_basic_addition(self, capsys):
        """Test basic addition with symbols"""
        result = processArithmetic("5 + 3")
        assert result == True
    
    def test_basic_subtraction(self, capsys):
        """Test basic subtraction with symbols"""
        result = processArithmetic("10 - 4")
        assert result == True
    
    def test_basic_multiplication(self, capsys):
        """Test basic multiplication with symbols"""
        result = processArithmetic("6 * 7")
        assert result == True
    
    def test_basic_division(self, capsys):
        """Test basic division with symbols"""
        result = processArithmetic("15 / 3")
        assert result == True
    
    def test_word_operations(self, capsys):
        """Test operations using words instead of symbols"""
        assert processArithmetic("5 plus 3") == True
        assert processArithmetic("10 minus 4") == True
        assert processArithmetic("6 times 7") == True
        assert processArithmetic("15 divided 3") == True
    
    def test_natural_language_questions(self, capsys):
        """Test natural language questions"""
        assert processArithmetic("What is 5 + 6?") == True
        assert processArithmetic("what is 10 minus 3?") == True
        assert processArithmetic("Calculate 4 times 5") == True
    
    def test_comparison_operations(self, capsys):
        """Test comparison operations"""
        assert processArithmetic("Is 5 equal 5?") == True
        assert processArithmetic("5 > 3") == True
        assert processArithmetic("3 < 5") == True
        assert processArithmetic("Is -1 equal to 10?") == True
    
    def test_compound_expressions(self, capsys):
        """Test expressions like '10/4' as one word"""
        result = processArithmetic("what is 10/4?")
        assert result == True
    
    def test_punctuation_handling(self, capsys):
        """Test that punctuation is handled correctly"""
        assert processArithmetic("5 + 3?") == True
        assert processArithmetic("10 - 4!") == True
        assert processArithmetic("6 * 7.") == True
    
    def test_invalid_input(self, capsys):
        """Test invalid inputs that should return False"""
        assert processArithmetic("hello world") == False
        assert processArithmetic("5") == False  # Only one number
        assert processArithmetic("plus minus") == False  # No numbers
        assert processArithmetic("") == False  # Empty string
    
    def test_negative_numbers(self, capsys):
        """Test operations with negative numbers"""
        assert processArithmetic("-5 + 3") == True
        assert processArithmetic("10 - -4") == True

class TestPrintFunctions:
    """Test cases for print functions from faker.py"""
    
    def test_print_greeting(self, capsys):
        """Test that greeting prints expected content"""
        printGreeting()
        captured = capsys.readouterr()
        assert "Hello!" in captured.out
        assert "silly goose" in captured.out
        assert "arithmetic" in captured.out
    
    def test_print_exit(self, capsys):
        """Test that exit message prints expected content"""
        printExit()
        captured = capsys.readouterr()
        assert "Thank you" in captured.out
        assert "Goodbye" in captured.out
    
    def test_print_error_processing(self, capsys):
        """Test that error message prints expected content"""
        printErrorProcessing()
        captured = capsys.readouterr()
        assert "Yikes" in captured.out
        assert "didn't understand" in captured.out
        assert "rephrase" in captured.out
    
    def test_print_help(self, capsys):
        """Test that help message prints expected content"""
        printHelp()
        captured = capsys.readouterr()
        assert "examples" in captured.out
        assert "5 + 6" in captured.out
        assert "stop" in captured.out

class TestIntegration:
    """Integration tests combining multiple functions"""
    
    def test_full_arithmetic_workflow(self, capsys):
        """Test complete workflow from input to output"""
        # Test that processArithmetic correctly uses calculate function
        result = processArithmetic("What is 8 + 7?")
        assert result == True
        
        # Test division by zero workflow
        result = processArithmetic("10 / 0")
        assert result == True  # Should still return True but with error message
    
    def test_boolean_operations_workflow(self, capsys):
        """Test boolean comparison workflow"""
        result = processArithmetic("Is 5 equal 5?")
        assert result == True
        
        result = processArithmetic("Is 10 greater 5?")
        assert result == True

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

@pytest.mark.parametrize("input_str,expected", [
    ("5 + 3", True),
    ("5+3", True),
    ("5+3?", True),
    ("10 - 4", True),
    ("6 * 7", True),
    ("15 / 3", True),
    ("What is 5 + 6?", True),
    ("Is -5 equal 5?", True),
    ("Is 5 equal to 5?", True),
    ("hello world", False),
    ("", False),
    ("5", False),
])
def test_process_arithmetic_parametrized(input_str, expected, capsys):
    """Parametrized test for processArithmetic function"""
    assert processArithmetic(input_str) == expected

# Fixtures for test data
@pytest.fixture
def arithmetic_test_cases():
    """Fixture providing test cases for arithmetic operations"""
    return [
        ("5 + 3", 8),
        ("10 - 4", 6),
        ("6 * 7", 42),
        ("15 / 3", 5),
        ("5+3", 8),
        ("10-4", 6),
        ("6*7", 42),
        ("15/3", 5),
        ("What is 5 + 6?", 11),
        ("Is -5 equal 5?", False),
        ("Is 5 equal to 5?", True),
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

def test_arithmetic_with_fixture(arithmetic_test_cases, capsys):
    """Test arithmetic operations using fixture data"""
    for input_str, expected in arithmetic_test_cases:
        result = processArithmetic(input_str)
        assert result == True

def test_comparison_with_fixture(comparison_test_cases, capsys):
    """Test comparison operations using fixture data"""
    for input_str, expected in comparison_test_cases:
        result = processArithmetic(input_str)
        assert result == True