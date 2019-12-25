'''
Created on Dec 25, 2019

@author: ashis
'''
from flask import Flask
from flask import render_template
app=Flask('__name__')
@app.route('/')
@app.route('/index')
def hello():
    user={'username':'Sainath'}
    car={'Electric':'Tesla'}
    return render_template('content.html',title='Sample',user=user,car=car)
    
if __name__=='__main__':
    app.run()
