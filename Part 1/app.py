from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.today().strftime('%Y-%m-%d')
    return f'Hello! This is Docker Compose Flask Date App!! Today is {today}!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')