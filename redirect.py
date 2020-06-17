from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello"

@app.route("/hello/<name>")
def route(name):
    return redirect(url_for('hello'))

if __name__=="__main__":
    app.run()
