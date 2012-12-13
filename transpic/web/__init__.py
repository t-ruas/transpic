
from flask import Flask

app = Flask(__name__)

from transpic.web import views

if __name__ == "__main__":
    app.run(debug=True)
