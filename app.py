from flask import Flask
app = Flask(__name__)

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "exception", 500

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/crash")
def crash():
    app.logger.info("crash route")
    a = 0
    b = 3 / a