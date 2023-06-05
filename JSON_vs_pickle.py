# Create a dictionary and write it in 3 fromats:
# python file, pickle file and JSON file.

import random
import pickle
import json

letters = "abcdefghijklmnopqrstuvwxyz"
d = {
    " ".join(random.choices(letters, k=6)): random.choice([True, False])
    for _ in range(100000)
}

# 1. Python file
#  write a python file
with open("mydict.py", "w") as fp:
    fp.write("d={\n")
    for k, v in d.items():
        fp.write(f"'{k}':{v},\n")
    fp.write("None:False}")

# read python file
# first import the file
"""from mydict import d """  # not working

# 2. pickle file
# write a pickle file
with open("mydict.pickle", "wb") as fb:
    pickle.dump(d, fb)

# read pickle file
with open("mydict.pickle", "rb") as fb:
    pickle.load(fb)

# 3. JSON
# write a JSON file
with open("mydict.json", "w") as fb:
    json.dump(d, fb)

# read JSON file
with open("mydict.json", "r") as fb:
    json.load(fb)

# of faster version: use ujson
"""import ujson 

with open("mydict.json", "r") as fb:
    ujson.load(fb)
"""  # not working
