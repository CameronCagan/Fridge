import requests
p = {'item' : 'apple'}
r = requests.get('http://127.0.0.1:5000/get', params = p )
print(r.text)