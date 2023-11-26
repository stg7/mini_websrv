#!/usr/bin/env python3
import time

import requests

print("start client")

try:
    x = requests.get('http://localhost:10000')
    print(x.text)
except Exception as e:
    print("error")

print("wait")

time.sleep(10)

