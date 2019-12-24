'''
Created on Dec 24, 2019

@author: ashish
'''

from flask import Flask
from flask import render_template
app=Flask("__name__")

@app.route('/')
@app.route('/index')
def get_index():
    user={"username":"Sainath"}
    return render_template("index.html",title='Home',user=user)
    
if __name__=="__main__":
    app.run()
    
    
