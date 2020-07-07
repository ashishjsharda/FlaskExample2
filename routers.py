from flask import Flask
app=Flask(__name__)
@app.route("/hello/<input>")
def input(input):
    return "Hello %s" % input
if __name__=='__main__':
    app.run()
