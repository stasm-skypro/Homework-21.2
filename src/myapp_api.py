import requests


url = "https://github.com/stasm-skypro/Homework-21.2.git#contacts.html"

response = requests.get(url)
if response.status_code == 200:
    print("OK!")
    print("Requested page content:")
    print(response.text)
else:
    print("Request error %s" %response.status_code)
