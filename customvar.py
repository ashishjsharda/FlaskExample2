'''
Created on Jan 20, 2020

@author: ashish
'''
from flask import Flask
app=Flask('__name__')
@app.route('/hello/<name>')
def hello_world(name):
    return "Hello %s" %name
if __name__=='__main__':
    app.run()
