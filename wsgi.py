from flask import Flask
import socket

application = Flask(__name__)

@application.route("/")
def hello():
    return socket.gethostname() + " says 'Hello World!'"


if __name__ == "__main__":
    application.run()
