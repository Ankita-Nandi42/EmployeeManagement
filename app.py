#Employee managemnet portal -Application entry point
#Flask application structure will be added here
from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
return"Employee Managemnet Prtal"

if __name__=="__main__":
app.run(debug=True)

