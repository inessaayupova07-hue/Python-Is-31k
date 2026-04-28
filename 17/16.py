import json

with open('data.json','r') as f:
    print(json.load(f))