#!/usr/bin/env python3
"""A command-line calculator that supports basic arithmetic operations."""

import argparse
import sys


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b.
    
    Args:
        a: The numerator
        b: The denominator
        
    Returns:
        The result of a / b
        
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def main():
    """Main entry point for the calculator CLI."""
    parser = argparse.ArgumentParser(
        description="A command-line calculator for basic arithmetic operations"
    )
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="The arithmetic operation to perform"
    )
    parser.add_argument(
        "a",
        type=float,
        help="The first operand"
    )
    parser.add_argument(
        "b",
        type=float,
        help="The second operand"
    )
    
    args = parser.parse_args()
    
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    
    try:
        result = operations[args.operation](args.a, args.b)
        print(f"Result: {result}")
        return 0
    except ZeroDivisionError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
