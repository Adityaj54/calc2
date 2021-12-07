""" This is Data test file from csv"""
import pytest
from calc.calculations.datamanager import DataManager
from calc.calculator import Calculator

# pylint: disable=unused-argument,redefined-outer-name,consider-using-with
f = open("/home/myuser/tests/test_data/log.txt", "w", encoding='utf-8', errors='ignore')
err = open("/home/myuser/tests/test_data/log_execption.txt", "w",
           encoding='utf-8', errors='ignore')


# pylint: disable=unused-argument,redefined-outer-name
@pytest.fixture
def get_data_fixture():
    """ THIS will get the data"""
    f.write('\n\nGETTING DATA \n')
    return DataManager.get_data('/home/myuser/tests/test_data/addition.csv')


# pylint: disable=unused-argument,redefined-outer-name
# using Tuple instead of args because we can pack as much data as we need into the tuple
@pytest.fixture
def test_generate_data_fixture():
    """This will generate the data"""
    return DataManager().generate_data()


def test_data_addition(get_data_fixture):
    """ this will add the data"""
    f.write('ADDITION')
    f.write('\n\n ===========\n')
    for row in get_data_fixture:
        Calculator.add_numbers(row)
        f.write(f'ADDITING TWO NUMBERS {row[0]},{row[1]} = {row[0] + row[1]} \n')
        print(Calculator.get_last_result_value(), row[0] + row[1])
        assert Calculator.get_last_result_value() == row[0] + row[1]


def test_data_multiplication(get_data_fixture):
    """ this will multiply the data"""
    f.write('MULTIPLICATION')
    f.write('\n\n ===========\n')
    for row in get_data_fixture:
        f.write(f'MULTIPLY TWO NUMBERS {row[0]},{row[1]} = {row[0] * row[1]} \n')
        Calculator.multiply_numbers(row)
        print(Calculator.get_last_result_value(), row[0] * row[1])
        assert Calculator.get_last_result_value() == row[0] * row[1]


def test_data_division(get_data_fixture):
    """ this will divide the data"""
    f.write('DIVISION\n')
    f.write('\n\n ===========\n')
    for row in get_data_fixture:

        if row[1] != 0:
            f.write(f'DIVIDE TWO NUMBERS {row[0]},{row[1]} = {row[0] / row[1]} \n')
            Calculator.divide_numbers(row)
            print(Calculator.get_last_result_value(), row[0], row[1])
            assert Calculator.get_last_result_value() == row[0] / row[1]
        else:
            Calculator.divide_numbers(row)
            err.write(f'DIVIDE TWO NUMBERS {row[0]},{row[1]}    => DIVIDE BY ZERO EXEC')
            print("Exception", row[0], row[1])
            with pytest.raises(ZeroDivisionError):
                Calculator.get_last_result_value()


def test_data_addition_generated_data(test_generate_data_fixture):
    """ this will add the data generated"""
    path = test_generate_data_fixture
    print(path)
    data_frame = DataManager.get_data(path)
    for row in data_frame:
        Calculator.add_numbers(row[1:3])
        print(Calculator.get_last_result_value(), row[3])
        assert Calculator.get_last_result_value() == row[3]


def test_data_multiplication_generated_data(test_generate_data_fixture):
    """ this will multiply the data generated"""
    path = test_generate_data_fixture
    data_frame = DataManager.get_data(path)
    for row in data_frame:
        Calculator.multiply_numbers(row[1:3])
        print(Calculator.get_last_result_value(), row[4])
        assert Calculator.get_last_result_value() == row[4]


def test_data_division_generated_data(test_generate_data_fixture):
    """ this will divide the data generated"""
    path = test_generate_data_fixture
    data_frame = DataManager.get_data(path)
    for row in data_frame:
        if row[2] != 0:
            Calculator.divide_numbers(row[1:3])
            print(Calculator.get_last_result_value(), row[5])
            assert round(Calculator.get_last_result_value(), 5) == round(row[5], 5)
        else:
            Calculator.divide_numbers(row[1:3])
            print("Exception")
            with pytest.raises(ZeroDivisionError):
                Calculator.get_last_result_value()
