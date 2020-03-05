from flask import Flask
app=Flask("__name__")
@app.route("/hello")
def hello_world():
    return "Hello World"

@app.route("/hello/admin")
def hello_admin():
    return "Hello Admin"

if __name__=="__main__":
    app.run()
