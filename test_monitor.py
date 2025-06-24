import pytest

from monitor import check_voltage, check_temperature, check_gas_level

def test_check_temperature():
    assert check_temperature(60.0) == True
    assert check_temperature(70.0) == True
    assert check_temperature(75.0) == False

def test_check_gas_level():
    assert check_gas_level(800.0) == True
    assert check_gas_level(1000.0) == True
    assert check_gas_level(1200.0) == False

def test_check_voltage():
    assert check_voltage(5.0) == True
    assert check_voltage(4.4) == False
    assert check_voltage(9.0) == True
    assert check_voltage(10.0) == False