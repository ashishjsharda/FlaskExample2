import flask
from flask import request,jsonify

app = flask.Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    return '''
    <h1>Using Python Flask </h1>
    <p>Example using Flask</p>
    '''
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found </p>",404

if __name__=="__main__":
    app.run()
