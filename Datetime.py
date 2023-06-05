# Data and time module.

import datetime

# Default format: yyyy-mm-dd

# check what is inside datetime by useing dir
'''dir(datetime) 
# should be: works in Python Shell
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__',
 '__loader__','__name__', '__package__', '__spec__',
 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 
 'timedelta', 'timezone', 'tzinfo'] 
 '''
# more info:
'''
help(datetime)
# should be long list, but interesting:
Data and other attributes defined here:
     |  
     |  max = datetime.date(9999, 12, 31)
     |  
     |  min = datetime.date(1, 1, 1)
'''
# 1. Print DOB Guido van Rossum, creator of Python

gvr=datetime.date(1956,1,31)
print(gvr) # DOB 
print(gvr.year) # prints year only
print(gvr.month)
print(gvr.day)

# 2. Calculate time. 100 days from date(mill)

mill=datetime.date(2000,1,1)
dt=datetime.timedelta(100) # calcutate 100 days
print(mill + dt) # result: 2000-04-10, 
# '-'can be used to calculate date before date(mill)

# 3. Different default formats. More info at https://docs.python.org
# eg. we want full name of Day-name,Month-name, Day-#, Year

print(gvr.strftime('%A,%B %d,%Y')) 

# or modern method:

message='GvR was bornon {:%A,%B %d,%Y}.'
print(message.format(gvr))

# 4. Launch date and time of first racket sent by SpaceX

launch_date=datetime.date(2017,3,30)
launch_time=datetime.time(22,27,0)
launch_datetime=datetime.datetime(2017,3,30,22,27,0)

print('Launch date: ',launch_date)
print('Launch time: ',launch_time)
print('Launch date and time: ',launch_datetime)
print('Launch date and time. Minute only: ', launch_datetime.minute)
#  We can pick specific info (eg. minute or day) only.

# 5. Access current date and time.

now=datetime.datetime.today()
print('Now is:',now)

# 6. Convert strings to an object datatime eg. moon landing.

moon_landing='7/20/1969' # a string we want to change
moon_landing_datetime=datetime.datetime.strptime(moon_landing,'%m/%d/%Y')
print('Moon landing date and time is: ',moon_landing_datetime) # changes to an object