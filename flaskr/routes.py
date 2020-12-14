from flask import render_template, flash, request, redirect, url_for, jsonify
from flask_login import current_user, logout_user, login_required

from .app import app
from . import dba
from .forms import ProductForm, UserForm, LoginForm
from .info import info
from .models import Producto

@app.route('/')
def index():
    productos = dba.get_products()
    return render_template(
        'index.jinja',
        **info,
        productos=productos
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        dba.check_login(form.data)
        return redirect(url_for('index'))

    return render_template(
        'forms/quick_form.jinja',
        **info,
        form=form
    )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def create_user():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = UserForm()

    if form.validate_on_submit():
        dba.register_user(form.data)
        return redirect(url_for('index'))

    return render_template(
        'forms/quick_form.jinja',
        **info,
        form=form
    )

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_user():
    form = UserForm(obj=current_user)
    if form.validate_on_submit():
        dba.update_user(current_user.usuario_id, form)
    return render_template('forms/quick_form.jinja', **info, form=form)

@app.route('/product/register', methods=['GET', 'POST'])
def create_product():
    form = ProductForm()

    if form.validate_on_submit():
        dba.register_product(form.data)
        return redirect(url_for('index'))

    return render_template(
        'forms/quick_form.jinja',
        **info,
        form=form
    )

@app.route('/product/edit/<_id>', methods=['GET', 'POST'])
def edit_product(_id):
    form = ProductForm(obj=Producto.query.get(_id))

    if form.validate_on_submit():
        dba.update_product(_id, form)
        return redirect(url_for('index'))

    return render_template(
        'forms/quick_form.jinja',
        **info,
        form=form
    )

@app.route('/product/buy/<_id>', methods=['GET', 'POST'])
def buy_product(_id):
    flash("Cargar formulario de compra...", _id)
    if current_user.is_authenticated:
        pass
    else:
        pass
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.jinja'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.jinja'), 500