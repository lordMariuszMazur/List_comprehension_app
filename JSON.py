# JSON. Java Script Object Notation.
# It's small, lightweight, data format.
# Almost identical to dictionart, shorter than XML.
# It can be quickly parsed by browsers like JavaScript syntax.
# This is ideal format for transporting data between a client and a server or mobile App.

""" 
Key Methods:
json.load(f): Load JSON data from file (or file-like object).
json.loads(s): Load JSON data from string.
json.dump(j,f): Write JSON object to file (or file-like object).
json.dumps(j): Output JSON object as string.
"""
import json

# dir(json)

value = """
{'title': 'Gattica',
'cinematographer': 'Sławomir Idziak'
'release_year': 1997
'budget': null
'actors': ['Ethan Hawke', 'Uma Thurman', 'Jude Law'
'won_oscar': false 
} """
# JSON: null == Python: None
# JSON: false == Python: False
# JSON: true == Python: True

movie = json.loads(value)
movie
