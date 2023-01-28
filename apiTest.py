import requests

# DSH$32Rfdhu@'34
request = requests.post("https://fitness-api.itsme12453.repl.co/register", headers={ "authentication-key": "DSH$32Rfdhu@'34", "email": "1234@gmail.com", "password": "123£$dsaa", "fullname": "123" })

print(request.text)