#!/usr/bin/env python3
print('Simple IP Check by B14ckD347h')
import requests
import socket
import json

def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# doesn't even have to be reachable
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except Exception:
		IP = '127.0.0.1'
	finally:
		s.close()
	return IP

print('Local IP: {}'.format())

publicIP = requests.get('https://api.ipify.org').text
print('Public IP: {}'.format(publicIP))

try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen

url = 'https://geo.ipify.org/api/v2/country,city?apiKey=at_dwcn4iXIc8iIicgUyo263uYq0xQQw&ipAddress='+publicIP
data = urlopen(url).read().decode('utf8')
d = json.loads(data)
city = d['location']['city']
country = d['location']['country']
print('Location: {}, {}'.format(city, country))



