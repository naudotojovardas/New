# Write a fixture for reading a csv file. 
# In the fixture, make sure that each column is automatically converted from string to an appropriate python type. For example, the csv data:
# player_id,date,name,surname,score
# 57,2024-01-12,John,Doe,87.2
# ..
# should return a list where each columns type is integer, datetime, string, string, float. 
# Return this parsed CSV data from a fixture
# Write at least 5 tests using this fixture.

import pytest
import datetime
from data_try import data
from csv_parametrization import csv_data

def player_id(value):
    return int(value)

def date(value):
    return datetime.datetime.strptime(value, '%Y-%m-%d')

def name(value):
    return value

def surname(value):
    return value

def score(value):
    return float(value)


def read_csv(file):
    with open(file) as f:
        lines = f.readlines()
        header = lines[0].strip().split(',')
        data = []
        for line in lines[1:]:
            row = line.strip().split(',')
            row[0] = int(row[0])
            row[1] = datetime.datetime.strptime(row[1], '%Y-%m-%d')
            row[4] = float(row[4])
            data.append(row)
    return data

@pytest.fixture
def csv_data():
    return read_csv('data_try.py')

def test_csv_data(csv_data):
    assert csv_data[0] == [57, datetime.datetime(2024, 1, 12), 'John', 'Doe', 87.2]

def test_csv_data_length(csv_data):
    assert len(csv_data) == 2

@pytest.mark.parametrize('index,expected', [ (0, 57), (1, 58) ])

def test_player_id(csv_data, index, expected):
    assert csv_data[index][0] == expected

@pytest.mark.parametrize('index,expected', [ (0, datetime.datetime(2024, 1, 12)), (1, datetime.datetime(2024, 1, 13)) ])

def test_date(csv_data, index, expected):
    assert csv_data[index][1] == expected

@pytest.mark.parametrize('index,expected', [ (0, 'John'), (1, 'Jane') ])

def test_name(csv_data, index, expected):
    assert csv_data[index][2] == expected

@pytest.mark.parametrize('index,expected', [ (0, 'Doe'), (1, 'Smith') ])

def test_surname(csv_data, index, expected):
    assert csv_data[index][3] == expected

@pytest.mark.parametrize('index,expected', [ (0, 87.2), (1, 90.5) ])

def test_score(csv_data, index, expected):
    assert csv_data[index][4] == expected

