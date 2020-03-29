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
  'units':Config.get('currentconditions','units')
})
#request = urllib.Request('http://api.openweathermap.org/data/2.5/weather',urllib.urlencode(urldata))
#request = urllib2.Request('http://api.openweathermap.org/data/2.5/weather?q=NYC&units=imperial')

try: 
    weather_api = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?%s" % urldata)
    response = weather_api.read()
    response_dictionary = json.loads(response)

    current = response_dictionary['main']['temp']
    current_low = response_dictionary['main']['temp_min']
    current_high = response_dictionary['main']['temp_max']
    conditions = response_dictionary['weather'][0]['description']

    current = round(current,1)
    current_low = round(current_low,1)
    current_high = round(current_high,1)
    #print current
    #print current_low
    #print current_high
    #print conditions

    # reads current weather
    currentconditions = 'Weather conditions for today are ' + str(conditions) + ' with a current temperature of ' + str(current) + " degrees. "
#except urllib2.HTTPError, e:
#    currentconditions = 'Failed to connect to Open Weather Map.  '
#except urllib2.URLError, e:
#    currentconditions = 'Failed to connect to Open Weather Map.  '
#except Exception:
#    currentconditions = 'Failed to connect to Open Weather Map.  '

#if Config.get('main','debug') == str(1):
#  print currentconditions
