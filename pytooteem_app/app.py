from flask import Flask
from homepage import pytooteem_home_page

app = Flask(__name__)


@app.route('/')
def home_page():
    return pytooteem_home_page()

if __name__ == '__main__':
    app.run(port=5000)