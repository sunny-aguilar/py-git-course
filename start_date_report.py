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
    year = imput('Enter a value for the year: ')
    month = imput('Enter a value for the month: ')
    day = imput('Enter a value for the day: ')
    print()
    
    return datetime.datetime()