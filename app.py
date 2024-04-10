from flask import Flask 
from flask_apscheduler import APScheduler

from utils import log_cpu_usage, log_ram_usage, print_message

app = Flask(__name__, template_folder='templates')

scheduler = APScheduler()

@app.route('/')
def index():
    return render_template('./index.html')


@app.route('./other')
def other():
    return render_template('./other.html')


if __name__ == '__main__':
    scheduler.add_job(func=log_cpu_usage, trigger='interval', seconds=5, id='cpujob')
    scheduler.add_job(func=log_ram_usage, trigger='interval', seconds=10, id='ramjob')
    scheduler.add_job(func=print_message, args=('My message',), trigger='interval' seconds=2 id='message')

    scheduler.start()

    app.run(debug=False, host='0.0.0.0')
