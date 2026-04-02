"""Unit tests for the calculator module."""

import pytest
import sys
from io import StringIO
from calculator import add, subtract, multiply, divide, main


class TestArithmeticOperations:
    """Test suite for basic arithmetic operations."""
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 5) == 15
        assert add(0.5, 0.5) == 1.0
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5
        assert add(10, -5) == 5
    
    def test_add_zero(self):
        """Test addition with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 5) == 5
        assert subtract(3, 5) == -2
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-5, 3) == -8
        assert subtract(5, -3) == 8
    
    def test_subtract_zero(self):
        """Test subtraction with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(10, 5) == 50
        assert multiply(0.5, 2) == 1.0
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply(-2, -3) == 6
        assert multiply(-2, 3) == -6
        assert multiply(2, -3) == -6
    
    def test_multiply_zero(self):
        """Test multiplication with zero."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(6, 3) == 2
        assert divide(10, 5) == 2
        assert divide(7, 2) == 3.5
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-6, -3) == 2
        assert divide(-6, 3) == -2
        assert divide(6, -3) == -2
    
    def test_divide_by_zero(self):
        """Test that division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(5, 0)
        
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(0, 0)
    
    def test_divide_zero_by_number(self):
        """Test division of zero by a non-zero number."""
        assert divide(0, 5) == 0
        assert divide(0, -5) == 0


class TestCLI:
    """Test suite for CLI functionality."""
    
    def test_cli_add(self, monkeypatch, capsys):
        """Test CLI with add operation."""
        monkeypatch.setattr(sys, 'argv', ['calculator.py', 'add', '5', '3'])
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Result: 8.0" in captured.out
    
    def test_cli_subtract(self, monkeypatch, capsys):
        """Test CLI with subtract operation."""
        monkeypatch.setattr(sys, 'argv', ['calculator.py', 'subtract', '10', '3'])
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Result: 7.0" in captured.out
    
    def test_cli_multiply(self, monkeypatch, capsys):
        """Test CLI with multiply operation."""
        monkeypatch.setattr(sys, 'argv', ['calculator.py', 'multiply', '4', '5'])
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Result: 20.0" in captured.out
    
    def test_cli_divide(self, monkeypatch, capsys):
        """Test CLI with divide operation."""
        monkeypatch.setattr(sys, 'argv', ['calculator.py', 'divide', '10', '2'])
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Result: 5.0" in captured.out
    
    def test_cli_divide_by_zero(self, monkeypatch, capsys):
        """Test CLI divide by zero error handling."""
        monkeypatch.setattr(sys, 'argv', ['calculator.py', 'divide', '10', '0'])
        result = main()
        captured = capsys.readouterr()
        assert result == 1
        assert "Error: Cannot divide by zero" in captured.err
    
    def test_cli_with_floats(self, monkeypatch, capsys):
        """Test CLI with floating point numbers."""
        monkeypatch.setattr(sys, 'argv', ['calculator.py', 'add', '2.5', '3.5'])
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Result: 6.0" in captured.out
    
    def test_cli_with_negative_numbers(self, monkeypatch, capsys):
        """Test CLI with negative numbers."""
        monkeypatch.setattr(sys, 'argv', ['calculator.py', 'add', '-5', '3'])
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Result: -2.0" in captured.out
