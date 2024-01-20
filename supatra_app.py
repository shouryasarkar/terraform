from flask import Flask
import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def hello_world():
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.datetime.now(eastern)
    return f'Hello, World! Current time in Eastern timezone: {current_time}'

if __name__ == '__main__':
    app.run(debug=True)

