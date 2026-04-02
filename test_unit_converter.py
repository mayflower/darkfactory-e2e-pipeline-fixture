"""
Tests for the unit converter CLI.
"""

import pytest
from unit_converter import (
    UnitConverter,
    convert_temperature,
    convert_distance,
    convert_weight,
)


class TestUnitConverter:
    """Test the UnitConverter class methods."""

    def test_celsius_to_fahrenheit(self):
        """Test Celsius to Fahrenheit conversion."""
        assert UnitConverter.celsius_to_fahrenheit(0) == 32
        assert UnitConverter.celsius_to_fahrenheit(100) == 212
        assert abs(UnitConverter.celsius_to_fahrenheit(37) - 98.6) < 0.1

    def test_celsius_to_kelvin(self):
        """Test Celsius to Kelvin conversion."""
        assert UnitConverter.celsius_to_kelvin(0) == 273.15
        assert UnitConverter.celsius_to_kelvin(-273.15) == 0
        assert UnitConverter.celsius_to_kelvin(100) == 373.15

    def test_fahrenheit_to_celsius(self):
        """Test Fahrenheit to Celsius conversion."""
        assert UnitConverter.fahrenheit_to_celsius(32) == 0
        assert UnitConverter.fahrenheit_to_celsius(212) == 100
        assert abs(UnitConverter.fahrenheit_to_celsius(98.6) - 37) < 0.1

    def test_fahrenheit_to_kelvin(self):
        """Test Fahrenheit to Kelvin conversion."""
        assert UnitConverter.fahrenheit_to_kelvin(32) == 273.15
        assert abs(UnitConverter.fahrenheit_to_kelvin(212) - 373.15) < 0.01

    def test_kelvin_to_celsius(self):
        """Test Kelvin to Celsius conversion."""
        assert UnitConverter.kelvin_to_celsius(273.15) == 0
        assert UnitConverter.kelvin_to_celsius(373.15) == 100
        assert UnitConverter.kelvin_to_celsius(0) == -273.15

    def test_kelvin_to_fahrenheit(self):
        """Test Kelvin to Fahrenheit conversion."""
        assert UnitConverter.kelvin_to_fahrenheit(273.15) == 32
        assert abs(UnitConverter.kelvin_to_fahrenheit(373.15) - 212) < 0.01

    def test_km_to_miles(self):
        """Test kilometers to miles conversion."""
        assert abs(UnitConverter.km_to_miles(1) - 0.621371) < 0.0001
        assert abs(UnitConverter.km_to_miles(5) - 3.106855) < 0.0001
        assert abs(UnitConverter.km_to_miles(10) - 6.21371) < 0.0001

    def test_miles_to_km(self):
        """Test miles to kilometers conversion."""
        assert abs(UnitConverter.miles_to_km(1) - 1.60934) < 0.0001
        assert abs(UnitConverter.miles_to_km(5) - 8.0467) < 0.0001
        assert abs(UnitConverter.miles_to_km(10) - 16.0934) < 0.0001

    def test_kg_to_lbs(self):
        """Test kilograms to pounds conversion."""
        assert abs(UnitConverter.kg_to_lbs(1) - 2.20462) < 0.0001
        assert abs(UnitConverter.kg_to_lbs(10) - 22.0462) < 0.0001
        assert abs(UnitConverter.kg_to_lbs(68) - 149.91416) < 0.001

    def test_lbs_to_kg(self):
        """Test pounds to kilograms conversion."""
        assert abs(UnitConverter.lbs_to_kg(1) - 0.453592) < 0.0001
        assert abs(UnitConverter.lbs_to_kg(10) - 4.53592) < 0.0001
        assert abs(UnitConverter.lbs_to_kg(150) - 68.0388) < 0.001


class TestTemperatureConversion:
    """Test temperature conversion function."""

    def test_same_unit_returns_same_value(self):
        """Test that converting to the same unit returns the same value."""
        assert convert_temperature(100, 'C', 'C') == 100
        assert convert_temperature(50, 'F', 'F') == 50
        assert convert_temperature(300, 'K', 'K') == 300

    def test_celsius_conversions(self):
        """Test Celsius conversions."""
        assert convert_temperature(0, 'C', 'F') == 32
        assert convert_temperature(100, 'C', 'K') == 373.15

    def test_fahrenheit_conversions(self):
        """Test Fahrenheit conversions."""
        assert convert_temperature(32, 'F', 'C') == 0
        assert abs(convert_temperature(32, 'F', 'K') - 273.15) < 0.01

    def test_kelvin_conversions(self):
        """Test Kelvin conversions."""
        assert convert_temperature(273.15, 'K', 'C') == 0
        assert abs(convert_temperature(273.15, 'K', 'F') - 32) < 0.01

    def test_case_insensitivity(self):
        """Test that unit conversion is case insensitive."""
        assert convert_temperature(100, 'c', 'f') == convert_temperature(100, 'C', 'F')
        assert convert_temperature(100, 'C', 'k') == convert_temperature(100, 'C', 'K')

    def test_invalid_units_raise_error(self):
        """Test that invalid units raise ValueError."""
        with pytest.raises(ValueError, match="Invalid temperature conversion"):
            convert_temperature(100, 'C', 'X')
        with pytest.raises(ValueError, match="Invalid temperature conversion"):
            convert_temperature(100, 'X', 'F')


class TestDistanceConversion:
    """Test distance conversion function."""

    def test_same_unit_returns_same_value(self):
        """Test that converting to the same unit returns the same value."""
        assert convert_distance(10, 'km', 'km') == 10
        assert convert_distance(5, 'mi', 'mi') == 5

    def test_km_to_miles_conversion(self):
        """Test kilometers to miles conversion."""
        assert abs(convert_distance(5, 'km', 'mi') - 3.106855) < 0.0001

    def test_miles_to_km_conversion(self):
        """Test miles to kilometers conversion."""
        assert abs(convert_distance(5, 'mi', 'km') - 8.0467) < 0.0001

    def test_case_insensitivity(self):
        """Test that unit conversion is case insensitive."""
        assert convert_distance(5, 'KM', 'MI') == convert_distance(5, 'km', 'mi')

    def test_invalid_units_raise_error(self):
        """Test that invalid units raise ValueError."""
        with pytest.raises(ValueError, match="Invalid distance conversion"):
            convert_distance(100, 'km', 'ft')
        with pytest.raises(ValueError, match="Invalid distance conversion"):
            convert_distance(100, 'meter', 'mi')


class TestWeightConversion:
    """Test weight conversion function."""

    def test_same_unit_returns_same_value(self):
        """Test that converting to the same unit returns the same value."""
        assert convert_weight(50, 'kg', 'kg') == 50
        assert convert_weight(100, 'lb', 'lb') == 100

    def test_kg_to_lbs_conversion(self):
        """Test kilograms to pounds conversion."""
        assert abs(convert_weight(68, 'kg', 'lb') - 149.91416) < 0.001

    def test_lbs_to_kg_conversion(self):
        """Test pounds to kilograms conversion."""
        assert abs(convert_weight(150, 'lb', 'kg') - 68.0388) < 0.001

    def test_case_insensitivity(self):
        """Test that unit conversion is case insensitive."""
        assert convert_weight(50, 'KG', 'LB') == convert_weight(50, 'kg', 'lb')

    def test_invalid_units_raise_error(self):
        """Test that invalid units raise ValueError."""
        with pytest.raises(ValueError, match="Invalid weight conversion"):
            convert_weight(100, 'kg', 'oz')
        with pytest.raises(ValueError, match="Invalid weight conversion"):
            convert_weight(100, 'gram', 'lb')


class TestEdgeCases:
    """Test edge cases and special values."""

    def test_negative_values(self):
        """Test that negative values work correctly."""
        assert convert_temperature(-40, 'C', 'F') == -40  # -40C = -40F
        assert convert_distance(-5, 'km', 'mi') < 0
        assert convert_weight(-10, 'kg', 'lb') < 0

    def test_zero_values(self):
        """Test zero values."""
        assert convert_temperature(0, 'C', 'F') == 32
        assert convert_distance(0, 'km', 'mi') == 0
        assert convert_weight(0, 'kg', 'lb') == 0

    def test_large_values(self):
        """Test large values."""
        result = convert_temperature(1000, 'C', 'F')
        assert result > 1000
        result = convert_distance(10000, 'km', 'mi')
        assert result > 0
        result = convert_weight(10000, 'kg', 'lb')
        assert result > 10000

    def test_decimal_values(self):
        """Test decimal values."""
        result = convert_temperature(37.5, 'C', 'F')
        assert abs(result - 99.5) < 0.1
        result = convert_distance(5.5, 'km', 'mi')
        assert result > 0
        result = convert_weight(68.5, 'kg', 'lb')
        assert result > 0
