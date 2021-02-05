from flask import Flask, render_template
from views.web.category import category

app = Flask(__name__)
app.register_blueprint(category)

name = 'olist'
menu = [
    {'name': 'Categories',
     'route': '/category'},
]


@app.route('/')
def index():
    return render_template('index.html', name=name, list=menu)


app.run(debug=True)