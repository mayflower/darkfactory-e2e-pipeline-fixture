#!/usr/bin/env python3
"""
Unit Converter CLI
Converts between temperature (C/F/K), distance (km/mi), and weight (kg/lb) units.
"""

import argparse
import sys


class UnitConverter:
    """Handles conversion between different units."""

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        """Convert Celsius to Kelvin."""
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        """Convert Fahrenheit to Kelvin."""
        celsius = UnitConverter.fahrenheit_to_celsius(fahrenheit)
        return UnitConverter.celsius_to_kelvin(celsius)

    @staticmethod
    def kelvin_to_celsius(kelvin):
        """Convert Kelvin to Celsius."""
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        """Convert Kelvin to Fahrenheit."""
        celsius = UnitConverter.kelvin_to_celsius(kelvin)
        return UnitConverter.celsius_to_fahrenheit(celsius)

    @staticmethod
    def km_to_miles(km):
        """Convert kilometers to miles."""
        return km * 0.621371

    @staticmethod
    def miles_to_km(miles):
        """Convert miles to kilometers."""
        return miles * 1.60934

    @staticmethod
    def kg_to_lbs(kg):
        """Convert kilograms to pounds."""
        return kg * 2.20462

    @staticmethod
    def lbs_to_kg(lbs):
        """Convert pounds to kilograms."""
        return lbs * 0.453592


def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between C, F, and K."""
    if from_unit == to_unit:
        return value

    converter = UnitConverter()
    conversion_map = {
        ('C', 'F'): converter.celsius_to_fahrenheit,
        ('C', 'K'): converter.celsius_to_kelvin,
        ('F', 'C'): converter.fahrenheit_to_celsius,
        ('F', 'K'): converter.fahrenheit_to_kelvin,
        ('K', 'C'): converter.kelvin_to_celsius,
        ('K', 'F'): converter.kelvin_to_fahrenheit,
    }

    key = (from_unit.upper(), to_unit.upper())
    if key not in conversion_map:
        raise ValueError(f"Invalid temperature conversion: {from_unit} to {to_unit}")

    return conversion_map[key](value)


def convert_distance(value, from_unit, to_unit):
    """Convert distance between km and mi."""
    if from_unit == to_unit:
        return value

    converter = UnitConverter()
    conversion_map = {
        ('km', 'mi'): converter.km_to_miles,
        ('mi', 'km'): converter.miles_to_km,
    }

    key = (from_unit.lower(), to_unit.lower())
    if key not in conversion_map:
        raise ValueError(f"Invalid distance conversion: {from_unit} to {to_unit}")

    return conversion_map[key](value)


def convert_weight(value, from_unit, to_unit):
    """Convert weight between kg and lb."""
    if from_unit == to_unit:
        return value

    converter = UnitConverter()
    conversion_map = {
        ('kg', 'lb'): converter.kg_to_lbs,
        ('lb', 'kg'): converter.lbs_to_kg,
    }

    key = (from_unit.lower(), to_unit.lower())
    if key not in conversion_map:
        raise ValueError(f"Invalid weight conversion: {from_unit} to {to_unit}")

    return conversion_map[key](value)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Unit Converter CLI - Convert between temperature, distance, and weight units',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s temperature 100 C F       # Convert 100 Celsius to Fahrenheit
  %(prog)s distance 5 km mi          # Convert 5 kilometers to miles
  %(prog)s weight 150 lb kg          # Convert 150 pounds to kilograms
        """
    )

    parser.add_argument(
        'category',
        choices=['temperature', 'distance', 'weight'],
        help='Category of conversion'
    )
    parser.add_argument(
        'value',
        type=float,
        help='Value to convert'
    )
    parser.add_argument(
        'from_unit',
        help='Unit to convert from (e.g., C, F, K, km, mi, kg, lb)'
    )
    parser.add_argument(
        'to_unit',
        help='Unit to convert to (e.g., C, F, K, km, mi, kg, lb)'
    )

    args = parser.parse_args()

    try:
        if args.category == 'temperature':
            result = convert_temperature(args.value, args.from_unit, args.to_unit)
        elif args.category == 'distance':
            result = convert_distance(args.value, args.from_unit, args.to_unit)
        elif args.category == 'weight':
            result = convert_weight(args.value, args.from_unit, args.to_unit)
        else:
            print(f"Error: Unknown category '{args.category}'", file=sys.stderr)
            sys.exit(1)

        print(f"{args.value} {args.from_unit} = {result:.2f} {args.to_unit}")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
