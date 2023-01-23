import requests

# DSH$32Rfdhu@'34
request = requests.post("https://fitness-app-hxjw.onrender.com/register", headers={ "authentication-key": "DSH$32Rfdhu@'34", "email": "123@gmail.com", "password": "123£$dsaa", "fullname": "123" })

print(request.text)