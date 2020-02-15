from flask import Flask,request,jsonify
app=Flask(__name__)
books = [
    {'id': 0,
     'title': 'Complete Reference Java',
     'author': 'Herbert Schildt',
     'first_sentence': 'Example using Complete Reference Java.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'Top 25 Leet Code Problems',
     'author': 'Ashish Sharda',
     'first_sentence': 'Top 25 Best Leet Code Problems',
     'published': '2019'}

]
@app.route('/',methods=['GET'])
def home():
    return '<h1>Reading Archive </h1><p>This site is prototype of reading novels</p>'
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)
app.run()
