'''
Created on Dec 22, 2019
Templates using Flask
@author: ashish
'''

from flask import Flask
app=Flask("__name__")
@app.route("/")
@app.route("/index")
def hello():
    user={'username':'Sai'}
    return '''
<html>
<head>
<title> This is ex using Flask </title>
</head>
<body>
<h1> Hello ''' +user['username'] + ''' !</h1>
</body>
</html>'''
if __name__=="__main__":
    app.run()

    
    

    

    
