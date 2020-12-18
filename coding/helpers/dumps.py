import json

def dumps(data):
    print(json.dumps(data, indent=4, default=str, sort_keys=True))