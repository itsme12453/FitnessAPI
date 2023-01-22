import requests

# DSH$32Rfdhu@'34
request = requests.post("http://127.0.0.1:8080/register", headers={ "authentication-key": "DSH$32Rfdhu@'34", "email": "123@gmail.com", "password": "123£$dsaa", "fullname": "123" })

print(request.text)