import requests

EMAIL = "123@gmail"
PASSWORD = "as23ds@@"
FULLNAME = "123"

# DSH$32Rfdhu@'34
request = requests.post(f"http://127.0.0.1:8080/register?email={EMAIL}&password={PASSWORD}&fullname={FULLNAME}", headers={ "authentication-key": "DSH$32Rfdhu@'34" })

print(request.text)