from flask import Flask
from flask_restful import Api

from resources.category_resource import CategoryResource

app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryResource, '/api/category', endpoint='categories')
api.add_resource(CategoryResource, '/api/category/<int:identifier>', endpoint='category')


@app.route('/')
def index():
    return 'API maneira!'


app.run(debug=True)
