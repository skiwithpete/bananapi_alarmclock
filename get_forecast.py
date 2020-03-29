#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import json
import decimal
import ConfigParser
Config=ConfigParser.ConfigParser()
try:
  Config.read('alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

urldata=urllib.urlencode({
  'q':Config.get('currentconditions','location'),
  'units':Config.get('currentconditions','units'),
  'cnt': 1
})

#request_2 = urllib2.Request('http://api.openweathermap.org/data/2.5/forecast/daily?q='+Config.get('forecast','location')+'&units='+Config.get('forecast','units')+'&cnt=1')
#request_2 = urllib2.Request('http://api.openweathermap.org/data/2.5/forecast/daily?q=NYC&units=imperial&cnt=1')

try: 
    forecast_api  = urllib.urlopen("http://api.openweathermap.org/data/2.5/forecast/daily?%s" % urldata)
    response_2 = forecast_api.read()
    response_2_dictionary = json.loads(response_2)

    todays_low = response_2_dictionary['list'][0]['temp']['night']
    todays_high = response_2_dictionary['list'][0]['temp']['day']

    todays_cond = response_2_dictionary['list'][0]['weather'][0]['description']

    todays_low = round(todays_low,1)
    todays_high = round(todays_high,1)
    
    #print todays_low
    #print todays_high

    # reads today’s forecast weather
    forecast = ' Todays forcast: ' + str(todays_cond) + ' with a high of ' + str(todays_high) + ' and an overnight low of ' + str(todays_low) + '.  '

except Exception:
    forecast = 'Failed to connect to Open Weather Map.  '

if Config.get('main','debug') == str(1):
  print forecast
