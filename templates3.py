'''
Created on Dec 24, 2019
Flask Example
@author: ashish
'''
from flask import Flask
app=Flask("__name__")

#Navigate on Localhost to / or index
@app.route("/")
@app.route("/index")
def hello():
    return "Hello World"
#Using Another Function
@app.route("/data")
def data():
    return "Hello Data"
#Using Template 
@app.route('/template')
def template():
    user={'username':'Sainath'}
    return '''
    <html>
    <h1> Username seen is ''' +user['username'] +'''</h1>
    </html>'''
if __name__=="__main__":
    app.run()

