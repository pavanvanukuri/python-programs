import configparser
config = configparser.ConfigParser()
config.read('config.ini')
host = config['DATABASE']['host']
user = config['DATABASE']['user']
password = config['DATABASE']['password']
port = config['SETTINGS']['port']
debug = config['SETTINGS']['debug']
print(host, user, password)
print(debug, port)
