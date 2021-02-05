from flask import request, render_template, Blueprint, redirect
from controllers.category_controller import CategoryController
from models.category import Category

category = Blueprint(__name__, 'category')
CONTROLLER = CategoryController()


@category.route('/category')
def list_all_categories():
    categories = CONTROLLER.read_all()
    return render_template('list_categories.html', name='olist', categories=categories)


@category.route('/category/create')
def create_category_form():
    return render_template('form_category.html', name='olist')


@category.route('/category/create', methods=['POST'])
def create_category():
    name = request.form.get('name')
    description = request.form.get('description')
    new_category = Category(name, description)
    if (name is None) and (description is None):
        return render_template('form_categories.html', name='olist')
    else:
        CONTROLLER.create(new_category)
        return redirect('/category')


@category.route('/category/update')
def update_get():
    id_ = request.args.get('id')
    print(id_)
    category = CONTROLLER.read_by_id(int(id_))
    return render_template('form_category.html', name='olist', edit=True, category=category)


@category.route('/category/update', methods=['POST'])
def update_post():
    id_ = request.form.get('id')
    print(id_)
    category = CONTROLLER.read_by_id(int(id_))
    category.name = request.form.get('name')
    category.description = request.form.get('description')
    CONTROLLER.update(category)
    return redirect('/category')


@category.route('/category/delete')
def delete():
    id_ = request.args.get('id')
    category = CONTROLLER.read_by_id(int(id_))
    CONTROLLER.delete(category)
    return redirect('/category')
