from django.http import request
from django.shortcuts import render
import requests
import json
# Create your views here.
def index(req):
    get_ip = requests.get('https://api.ipify.org?format=json')
    ip = json.loads(get_ip.text)
    res = requests.get('http://ip-api.com/json/'+ip['ip'])
    location_data = json.loads(res.text)    
    return render(req, 'index.html', {'data' : location_data})
