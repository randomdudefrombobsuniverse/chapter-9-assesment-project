from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm, AddProductForm


@app.route('/')
@app.route('/shop')
def shop():
    ''''Shop URL'''
    return render_template('Shop.html', title='Shop')


@app.route('/add_product')
def add_product():
    '''Add Product URL'''
    form = AddProductForm()
    return render_template('add_product.html', title='Add Product Page', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    '''Register URL'''
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You are requesting to login in {form.username.data}')
        return redirect(url_for('shop'))
    return render_template('register.html', title='Register Page', form=form)