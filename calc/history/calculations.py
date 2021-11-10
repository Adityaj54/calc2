"""Calculation history Class"""
class Calculations:
    """ Class """
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """ Clear history"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """ Count history"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """ gets calculation"""
        return Calculations.history[-1]
    @staticmethod
    def get_first_calculation():
        """ gets first calculationy"""
        return Calculations.history[-1]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
