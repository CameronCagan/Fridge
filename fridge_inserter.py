import requests
import json
item = {'beef'}
r = requests.put('http://127.0.0.1:5000/insert', params= {'item' : item})
print(r.text)   