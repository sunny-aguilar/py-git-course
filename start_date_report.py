#!/usr/bin/env python
import csv
import datetime
import requests

FILE_URL="http://marga.com/ar/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    year = int(imput('Enter a value for the year: '))
    month = int(imput('Enter a value for the month: ')
    day = int(imput('Enter a value for the day: ')
    print()
    
    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in thef ile at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)


