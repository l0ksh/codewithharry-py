#!/usr/bin/python3

#print("Twinkle Twinkle little star")

import requests

result = requests.get('https://cdac.in')

print(result.text)
