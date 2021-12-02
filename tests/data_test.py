from calc.calculations.datamanager import DataManager, get_data
import pytest
from calc.calculator import Calculator


@pytest.fixture
def get_data_fixture():
    return get_data('/home/myuser/tests/test_data/addition.csv')


@pytest.fixture
def test_generate_data_fixture():
    return DataManager().generate_data()


def test_data_addition(get_data_fixture):
    for row in get_data_fixture:
        Calculator.add_numbers(row)
        print(Calculator.get_last_result_value(), row[0] + row[1])
        assert Calculator.get_last_result_value() == row[0] + row[1]


def test_data_multiplication(get_data_fixture):
    for row in get_data_fixture:
        Calculator.multiply_numbers(row)
        print(Calculator.get_last_result_value(), row[0] * row[1])
        assert Calculator.get_last_result_value() == row[0] * row[1]


def test_data_division(get_data_fixture):
    for row in get_data_fixture:
        if row[1] != 0:
            Calculator.divide_numbers(row)
            print(Calculator.get_last_result_value(), row[0], row[1])
            assert Calculator.get_last_result_value() == row[0] / row[1]
        else:
            Calculator.divide_numbers(row)
            print("Exception", row[0], row[1])
            with pytest.raises(ZeroDivisionError):
                Calculator.get_last_result_value()


def test_data_addition_generated_data(test_generate_data_fixture):
    path = test_generate_data_fixture
    print(path)
    df = get_data(path)
    for row in df:
        Calculator.add_numbers(row[1:3])
        print(Calculator.get_last_result_value(), row[3])
        assert Calculator.get_last_result_value() == row[3]


def test_data_multiplication_generated_data(test_generate_data_fixture):
    path = test_generate_data_fixture
    df = get_data(path)
    for row in df:
        Calculator.multiply_numbers(row[1:3])
        print(Calculator.get_last_result_value(), row[4])
        assert Calculator.get_last_result_value() == row[4]


def test_data_division_generated_data(test_generate_data_fixture):
    path = test_generate_data_fixture
    df = get_data(path)
    for row in df:
        if row[2] != 0:
            Calculator.divide_numbers(row[1:3])
            print(Calculator.get_last_result_value(), row[5])
            assert round(Calculator.get_last_result_value(),5) == round(row[5],5)
        else:
            Calculator.divide_numbers(row[1:3])
            print("Exception")
            with pytest.raises(ZeroDivisionError):
                Calculator.get_last_result_value()
