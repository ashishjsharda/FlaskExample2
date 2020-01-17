'''
Created on Jan 17, 2020

@author: ashish
'''
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello Flask"
if __name__=='__main__':
    app.run()
