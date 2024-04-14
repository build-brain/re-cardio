import requests

url = "http://127.0.0.1:8000/admission_data/1/attach_file/"

payload = {"title": "Title"}
files=[
  ('file', ("Screenshot 2024-01-26 140808.png", open('C:/Users/dooss/Pictures/Screenshots/Screenshot 2024-01-26 140808.png', 'rb'), 'image/png'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)