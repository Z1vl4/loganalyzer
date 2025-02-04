
from flask import Flask


app = Flask(__name__)

@app.route('/')

#testa lägg in från html när den läggs in i (rätt) folder
def index():
    return "Hello World"


#error printas på hemsidan atm
if __name__ == "__main__":
    app.run(debug=True)
