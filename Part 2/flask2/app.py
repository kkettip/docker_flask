from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.today().strftime('%Y-%m-%d')
    return f'Hello from Flask App 2!!!! Today is {today}'

    #return 'Hello from Flask App 2!!!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')