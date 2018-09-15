# -*- coding: utf-8 -*-
"""
Five day weather scraper from OpenWeatherMap.org

Tampa, FL ID: 4174757
"""

import requests
from datetime import date

APIKEY = '{REDACTED}'
cityID = 4174757
url = f'https://api.openweathermap.org/data/2.5/forecast?id={cityID}&APPID={APIKEY}'

sauce = requests.get(url)
json_data = sauce.json()

def k_to_f(temp):
    """ Converts Kelvin temperature to fahrenheit.
        Input: float
        Output: float to one decimal place """    
    try:
        f = 1.8 * (temp - 273) + 32
        return round(f,1)
    except Exception as e:
        return None
    
def temp_low(a,b):
    """ Calculates the low temperature for the day. Integers
    'a' and 'b' are used for the ranges of information in the json. """
    
    temp_low = 0
    for num in range(a,b):
        temp_low += json_data['list'][num]['main']['temp_min']
        
    return temp_low/(b-a)

def temp_high(a,b):
    """ Calculates the high temperature for the day. Integers
    'a' and 'b' are used for the ranges of information in the json. """
    
    temp_high = 0
    for num in range(a,b):
        temp_high += json_data['list'][num]['main']['temp_max']
        
    return temp_high/(b-a)

def weather_conditions(a,b):
    """ Determines the weather condition for the day. Integers 'a' and 'b'
    are used for the ranges of information in the json. """
    
    for num in range(a,b):
        if json_data['list'][num]['dt_txt'].split(' ')[1] == '12:00:00':
            return json_data['list'][num]['weather'][0]['description']
    

# Finds the present day of the week as a string
weekdays = {0: 'Sunday',
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday'}

today = date.today().isoweekday()

week = f'{weekdays[today]: <{16}} {weekdays[(today+1)%7]:<{16}} '\
       f'{weekdays[(today+2)%7]:<{16}} {weekdays[(today+3)%7]:<{16}} '\
       f'{weekdays[(today+4)%7]:<{16}}'
        
dayOne = {'high': 0, 'low': 0, 'desc': ''}
dayTwo = {'high': 0, 'low': 0, 'desc': ''}
dayThree = {'high': 0, 'low': 0, 'desc': ''}
dayFour = {'high': 0, 'low': 0, 'desc': ''}
dayFive = {'high': 0, 'low': 0, 'desc': ''}

highest = len(json_data['list'])

dayOne['low'] = k_to_f(temp_low(0,7))
dayOne['high'] = k_to_f(temp_high(0,7))
dayOne['desc'] = weather_conditions(0,7)

dayTwo['low'] = k_to_f(temp_low(7,15))
dayTwo['high'] = k_to_f(temp_high(7,15))
dayTwo['desc'] = weather_conditions(7,15)

dayThree['low'] = k_to_f(temp_low(15,23))
dayThree['high'] = k_to_f(temp_high(15,23))
dayThree['desc'] = weather_conditions(15,23)

dayFour['low'] = k_to_f(temp_low(23,31))
dayFour['high'] = k_to_f(temp_high(23,31))
dayFour['desc'] = weather_conditions(23,31)

dayFive['low'] = k_to_f(temp_low(31,highest))
dayFive['high'] = k_to_f(temp_high(31,highest))
dayFive['desc'] = weather_conditions(31,highest)
    
print('*'*80)
print(week)
print(f"{dayOne['high']:<{16}} {dayTwo['high']:<{16}} {dayThree['high']:<{16}} " \
      f"{dayFour['high']:<{16}} {dayFive['high']:<{16}}")
print(f"{dayOne['low']:<{16}} {dayTwo['low']:<{16}} {dayThree['low']:<{16}} " \
      f"{dayFour['low']:<{16}} {dayFive['low']:<{16}}")
print(f"{dayOne['desc']:<{16}} {dayTwo['desc']:<{16}} {dayThree['desc']:<{16}} " \
      f"{dayFour['desc']:<{16}} {dayFive['desc']:<{16}}")
print('*'*80)
