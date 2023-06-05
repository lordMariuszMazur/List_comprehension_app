# Dictionaries(dict).
# Inputs are called keys and output are values.

post={'user_id':209,'message':'D5 E5 C5 C4 G4', 'language':'English',
'datatime':'20230215T124231Z', 'location':(44.590533, -104.715556)}

#type(post)
# should be: <class 'dict'>

post2=dict(message='SS Enterprise', language='English')

post2['user_id']=209
post2['datetime']='19771116T093001Z'

#print(post2)

# Accessing data in dictionaries.

#print(post['message'])

# 1. First way to check if there is data in dictionairy.
'''try:
    print(post2['location'])
except KeyError:
    print('The post does not have a location') '''

# 2. Second way.
'''
dir(post2)
help(post2.get) ''' # Gets details about dict post2

loc=post2.get('location', None) # if key location is missing it's returns None
#print(loc)

def return_dict():
    for key in post.keys():
        value=post[key]
        print(key, '=', value)

def another_way():
    for key, value in post.items():
        print(key, '=', value)

#z=another_way() # or return_dict()
#print(z)

# 3. Removing items from the dict.
'''pop and popitem methods remove a single item from a dict.
clear method remove all data from a dict. '''

#m=post.pop('location')
#print(m)