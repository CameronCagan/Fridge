import requests

item = {'apple'}
r = requests.delete('http://127.0.0.1:5000/remove', params= {'item' : item} )
print(r.text)