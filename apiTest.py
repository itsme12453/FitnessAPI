import requests

request = requests.post("http://192.168.0.97:8080/register", headers={ "authentication-key": "123", "email": "123@gmail.com", "password": "123£$dsaa", "fullname": "123" })

print(request.text)