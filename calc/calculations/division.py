""" THIS IS THE DIVISION CLASS"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """ calculation division class"""

    def get_result(self):
        """get the division results"""
        result = self.values[0]
        for i in self.values[1:]:
            try:
                result /= i
            except ZeroDivisionError as err:
                raise ZeroDivisionError from err
        return result
