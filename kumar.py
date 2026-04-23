import json

with open('pavan.json', 'r') as file:
    config = json.load(file)

host = config['DATABASE']['host']
port = config['DATABASE']['port']
debug = config['SETTINGS']['debug']

print(host, port, debug)
