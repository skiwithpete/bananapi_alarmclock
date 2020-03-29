#!/usr/bin/python
import time
import ConfigParser

# print time.strftime("%m%d")

Config=ConfigParser.ConfigParser()
try:
  Config.read('alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

if int(time.strftime("%m%d")) == 101 :
  birthday = 'Catriona'
if int(time.strftime("%m%d")) == 114 :
  birthday = 'Tranter'
if int(time.strftime("%m%d")) == 117 :
  birthday = 'Jodi'
if int(time.strftime("%m%d")) == 121 :
  birthday = 'Pat Foran'
if int(time.strftime("%m%d")) == 216 :
  birthday = 'Alana'
if int(time.strftime("%m%d")) == 216 :
  birthday = 'Schultz'
if int(time.strftime("%m%d")) == 304 :
  birthday = 'Meg'
if int(time.strftime("%m%d")) == 306 :
  birthday = 'Andrea'
if int(time.strftime("%m%d")) == 313 :
  birthday = 'Ron'
if int(time.strftime("%m%d")) == 315 :
  birthday = 'Uncle Dave'
if int(time.strftime("%m%d")) == 316 :
  birthday = 'Esther'
if int(time.strftime("%m%d")) == 319 :
  birthday = 'Julie Bauer'
if int(time.strftime("%m%d")) == 325 :
  birthday = 'Sylvia'
if int(time.strftime("%m%d")) == 327 :
  birthday = 'Kate Laird'
if int(time.strftime("%m%d")) == 331 :
  birthday = 'Diana and Tristan'
if int(time.strftime("%m%d")) == 402 :
  birthday = 'Samson and Arlo'
if int(time.strftime("%m%d")) == 403 :
  birthday = 'Adam Thompson'
if int(time.strftime("%m%d")) == 427 :
  birthday = 'Chloe'
if int(time.strftime("%m%d")) == 430 :
  birthday = 'ET'
if int(time.strftime("%m%d")) == 504 :
  birthday = 'Stephanie and Mitch'
if int(time.strftime("%m%d")) == 513 :
  birthday = 'Dad'
if int(time.strftime("%m%d")) == 522 :
  birthday = 'Heidi'
if int(time.strftime("%m%d")) == 528 :
  birthday = 'Levi'
if int(time.strftime("%m%d")) == 601 :
  birthday = 'Eilidh'
if int(time.strftime("%m%d")) == 605 :
  birthday = 'Caitlin'  
if int(time.strftime("%m%d")) == 607 :
  birthday = 'Trevor'
if int(time.strftime("%m%d")) == 623 :
  birthday = 'Dad and Erica'
if int(time.strftime("%m%d")) == 628 :
  birthday = 'Maya'
if int(time.strftime("%m%d")) == 629 :
  birthday = 'Jenny'
if int(time.strftime("%m%d")) == 705 :
  birthday = 'Dwayne'
if int(time.strftime("%m%d")) == 714 :
  birthday = 'Eryn Gravelle'
if int(time.strftime("%m%d")) == 804 :
  birthday = 'Matt Roberts'
if int(time.strftime("%m%d")) == 808 :
  birthday = 'Tante Simonne'
if int(time.strftime("%m%d")) == 810 :
  birthday = 'Natalie Bauer and Taylz'
if int(time.strftime("%m%d")) == 814 :
  birthday = 'Derek'
if int(time.strftime("%m%d")) == 817 :
  birthday = 'Kirsten'
if int(time.strftime("%m%d")) == 818 :
  birthday = 'Aunt Wendy'
if int(time.strftime("%m%d")) == 831 :
  birthday = 'Mark'
if int(time.strftime("%m%d")) == 908 :
  birthday = 'Kimmy'
if int(time.strftime("%m%d")) == 909 :
  birthday = 'Auntie Lu'
if int(time.strftime("%m%d")) == 911 :
  birthday = 'Ellason'
if int(time.strftime("%m%d")) == 913 :
  birthday = 'Meredith'
if int(time.strftime("%m%d")) == 915 :
  birthday = 'Mom'
if int(time.strftime("%m%d")) == 927 :
  birthday = 'Andrew'
if int(time.strftime("%m%d")) == 929 :
  birthday = 'Peter'
if int(time.strftime("%m%d")) == 1006 :
  birthday = 'Uncle Gary'
if int(time.strftime("%m%d")) == 1019 :
  birthday = 'Treeve'
if int(time.strftime("%m%d")) == 1020 :
  birthday = 'Julian'
if int(time.strftime("%m%d")) == 1025 :
  birthday = 'Aunt Nancy'
if int(time.strftime("%m%d")) == 1114 :
  birthday = 'Abbie'
if int(time.strftime("%m%d")) == 1120 :
  birthday = 'Wilton'
if int(time.strftime("%m%d")) == 1123 :
  birthday = 'Lachlainn'
if int(time.strftime("%m%d")) == 1126 :
  birthday = 'Kielback'
if int(time.strftime("%m%d")) == 1130 :
  birthday = 'Amy Boyle'
if int(time.strftime("%m%d")) == 1206 :
  birthday = 'Dom'
if int(time.strftime("%m%d")) == 1211 :
  birthday = 'Katherine'
if int(time.strftime("%m%d")) == 1212 :
  birthday = 'Gadd'
if int(time.strftime("%m%d")) == 1218 :
  birthday = 'Mom'
#if int(time.strftime("%m%d")) == 904 :
#  birthday = 'dummy'

else:
  birthday = 'null'

print birthday

# reads out birthday
if birthday == 'null':
  birthday = ''
else:
  birthday = 'Today is ' + birthday + 's birthday.  ' 

if Config.get('main','debug') == str(1):
  print birthday


