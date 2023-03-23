import requests
import json

url = "http://127.0.0.1:8000/api/specificstudent/3"

r = requests.get(url = url)

result = r.json()

print(result)