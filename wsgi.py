from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! Getting Started With Python!"

if __name__ == "__main__":
    application.run()
