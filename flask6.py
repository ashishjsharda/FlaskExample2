from flask import Flask
app=Flask(__name__)
@app.route("/hello/<int:id>")
def product_id(id):
    return "Hello %d"%id

if __name__=='__main__':
    app.run(debug=True)
