# Dark Factory E2E Pipeline Fixture

## Unit Converter CLI

A Python command-line interface tool for converting between different units.

### Features

- **Temperature Conversion**: Convert between Celsius (C), Fahrenheit (F), and Kelvin (K)
- **Distance Conversion**: Convert between kilometers (km) and miles (mi)
- **Weight Conversion**: Convert between kilograms (kg) and pounds (lb)

### Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

The CLI follows this format:

```bash
python unit_converter.py <category> <value> <from_unit> <to_unit>
```

#### Examples

**Temperature Conversion:**
```bash
python unit_converter.py temperature 100 C F      # 100 Celsius to Fahrenheit
python unit_converter.py temperature 32 F C       # 32 Fahrenheit to Celsius
python unit_converter.py temperature 273.15 K C   # 273.15 Kelvin to Celsius
```

**Distance Conversion:**
```bash
python unit_converter.py distance 5 km mi         # 5 kilometers to miles
python unit_converter.py distance 10 mi km        # 10 miles to kilometers
```

**Weight Conversion:**
```bash
python unit_converter.py weight 150 lb kg         # 150 pounds to kilograms
python unit_converter.py weight 68 kg lb          # 68 kilograms to pounds
```

### Help

To see all available options:

```bash
python unit_converter.py --help
```

### Input Validation

The CLI handles invalid input gracefully:
- Invalid category names (must be: temperature, distance, or weight)
- Invalid unit combinations (e.g., trying to convert km to F)
- Non-numeric values (must be valid numbers)
- Invalid units for each category

### Running Tests

Run the test suite using pytest:

```bash
pytest test_unit_converter.py
```

For verbose output:

```bash
pytest test_unit_converter.py -v
```

To see test coverage:

```bash
pytest test_unit_converter.py --cov=unit_converter --cov-report=term-missing
```

### Test Coverage

The test suite includes:
- Unit tests for all conversion methods
- Integration tests for the conversion functions
- Edge case testing (negative values, zero, large numbers, decimals)
- Input validation testing (invalid units, same-unit conversions)
- Case insensitivity testing

### Project Structure

```
.
├── unit_converter.py          # Main CLI application
├── test_unit_converter.py     # Test suite
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```
