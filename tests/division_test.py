"""Testing Subtraction"""
from calc.calculations.division import Division
import pytest



def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    # Arrange
    mynumbers = (4.0, 2.0)
    division = Division(mynumbers)
    # Act
    # Assert
    assert division.get_result() == 2.0


def test_calculation_division_err():
    """testing that our calculator has a static method for addition"""
    # Arrange
    mynumbers = (4.0, 0.0)
    division = Division(mynumbers)
    # Act
    # Assert
    with pytest.raises(ZeroDivisionError):
        division.get_result()



