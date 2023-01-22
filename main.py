from database import Database
from flask import Flask, request, make_response
import re

connectionString = "mongodb+srv://fitness1209:ma59T5fnb0AT1J3h@cluster0.iefjevr.mongodb.net/?retryWrites=true&w=majority"
database = Database(connectionString)

# details = database.find_data("Auth", { "test": "data" })
# details = database.insert_data("Auth", { "test": "data" })

# print(details)

app = Flask(__name__)
app.secret_key = "472389fhdsuf2378ghf"

@app.route("/register", methods=["POST"])
def home():
    #/register?email={EMAIL}&password={PASSWORD}&fullname={FULLNAME}

    email = request.headers["email"]
    password = request.headers["password"]
    fullname = request.headers["fullname"]

    secreyKey = request.headers.get("authentication-key")

    if secreyKey == "123":
        pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
        validEmail = bool(re.fullmatch(pattern, email))

        passwordPattern = re.compile(r"^(?=.*[0-9])(?=.*[!@#$%^&*£])[a-zA-Z0-9!@#$%^&*£]{6,16}$")
        validPassword = bool(re.fullmatch(passwordPattern, password))

        if(not validPassword or len(password) < 8 or not validEmail or len(str(fullname)) == 0):
            return make_response("Invalid Password or Email or Fullname", 406)

        if database.find_data("Auth", { "email": email }):
            return make_response("Email already exists", 406)
        
        database.insert_data("Auth", { "email": email, "password": password, "fullname": fullname })

        return make_response("Registered", 200)
    
    return make_response("Invalid Authentication", 401)

app.run(host="0.0.0.0", port=8080)