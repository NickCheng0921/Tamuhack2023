from flask import Flask, render_template
from flask import request
import sys 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sendRequest', methods=['POST'])
def sendRequest():
    title = request.form['titleInput']
    print(f'Request function was called w title {title} ! ', file=sys.stderr)
    return ('', 204)
