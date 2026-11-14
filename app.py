from flask import Flask
app=Flask(__name__)
@app.route("/")
def home:
return"Employee Managemnet portal"

@app.route("/register",methods=["POST"]
def register_employee():
return"Employee registered",201

@app.route("/search")
def search_employee():
return "search results"

if __name__=="__main__":
app.run(debug==True)

