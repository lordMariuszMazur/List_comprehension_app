# Object serialization from pickle to JSON

import pickle
import json

data = {
    "Name": "V",
    "Address": "Afterlife, Night City",
    "Telephone": 555666,
    "Hours on the case": 5,
    "Amount to bill": 310.0,
}

with open("sm.pickle", "wb") as fb:
    pickle.dump(data, fb)

with open("sm.pickle", "rb") as fb:
    data = pickle.load(fb)

bytes_sequence = pickle.dumps(data)

data = pickle.loads(bytes_sequence)

with open("sma.json", "w") as fb:
    json.dump(data, fb)

with open("sma.json", "r") as fb:
    data = json.load(fb)

json_str = json.dumps(data)

data = json.loads(json_str)

print(data)
