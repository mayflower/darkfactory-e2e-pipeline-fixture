# Calculator CLI Tool

A command-line calculator that supports basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- Support for four basic arithmetic operations (add, subtract, multiply, divide)
- Command-line interface using argparse
- Division by zero error handling
- Support for integer and floating-point numbers
- Comprehensive unit tests with pytest

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The calculator accepts three arguments:
1. `operation` - The arithmetic operation to perform (add, subtract, multiply, divide)
2. `a` - The first operand (number)
3. `b` - The second operand (number)

### Examples

```bash
# Addition
python calculator.py add 5 3
# Output: Result: 8.0

# Subtraction
python calculator.py subtract 10 3
# Output: Result: 7.0

# Multiplication
python calculator.py multiply 4 5
# Output: Result: 20.0

# Division
python calculator.py divide 10 2
# Output: Result: 5.0

# Division by zero (error handling)
python calculator.py divide 10 0
# Output: Error: Cannot divide by zero
```

### Using Negative Numbers

```bash
python calculator.py add -5 3
# Output: Result: -2.0
```

### Using Floating-Point Numbers

```bash
python calculator.py multiply 2.5 3.5
# Output: Result: 8.75
```

## Running Tests

Run the test suite using pytest:

```bash
pytest test_calculator.py
```

Run with verbose output:

```bash
pytest test_calculator.py -v
```

## Project Structure

```
.
├── calculator.py       # Main calculator module with CLI
├── test_calculator.py  # Unit tests for calculator
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Error Handling

The calculator handles the following error scenarios:

- **Division by zero**: Returns an error message and exits with code 1
- **Invalid input**: argparse handles invalid arguments and displays help message
- **Invalid operation**: argparse restricts operations to the four supported types
