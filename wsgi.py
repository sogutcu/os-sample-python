import socket
import time
import atexit

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler



application = Flask(__name__)

@application.route("/")
def hello():
    return socket.gethostname() + " says 'Hello World!'"

def tick():
    print(socket.gethostname() + time.strftime(" %A, %d. %B %Y %I:%M:%S %p"))

scheduler = BackgroundScheduler()
scheduler.add_job(func=tick, trigger="interval", seconds=5)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    application.run()
