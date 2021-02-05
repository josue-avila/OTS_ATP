from flask_restful import fields, marshal_with

from dao.category_dao import CategoryDao
from models.category import Category
from resources.base_resource import BaseResource


class CategoryResource(BaseResource):
    fields = {
        "id_": fields.Integer,
        "name": fields.String,
        "description": fields.String,
    }

    def __init__(self):
        self.__dao = CategoryDao()
        self.__model_type = Category

        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, identifier=None):
        return super().get(identifier)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, identifier):
        return super().put(identifier)

    @marshal_with(fields)
    def delete(self, identifier):
        return super().delete(identifier)
