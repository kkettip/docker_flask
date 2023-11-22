from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    
    today = datetime.today().strftime('%Y-%m-%d')
    return render_template('index.html', today=today)

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



