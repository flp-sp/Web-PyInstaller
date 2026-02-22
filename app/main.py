from flask import Flask, session

app = Flask(__name__)
app.secret_key = "1234" # talvez mudar

from routes import *

if __name__ == '__main__':
    app.run(debug=False)