from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Getting Started With Python!\n"

if __name__ == "__main__":
    application.run()
