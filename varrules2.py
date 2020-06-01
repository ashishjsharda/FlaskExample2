from flask import Flask
app=Flask(__name__)
@app.route('/hello/<name>')
def hello_name(name):
    return "Hello %s"%name

@app.route('/hello/<int:id>')
def purchase_id(id):
    return "Purchase Id is %d"%id

@app.route("/change/<float:change>")
def change(change):
    return "Change left is %f" %change

if __name__=='__main__':
    app.run(debug=True)
