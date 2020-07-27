from flask import render_template, url_for, flash, redirect
from ffgt import app
from ffgt.forms import RegistrationForm, LoginForm
from ffgt.models import User, Post


posts = [
    {
        'author': "Sravan",
        'title': 'Watch Blog',
        'content': 'First Post content',
        'date': 'April 20, 2020'
    },
    {
        'author': "Jayalakshmi",
        'title': 'Cooking Blog',
        'content': 'First Post about cooking',
        'date': 'July 20, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'sravanjsc@gmail.com' and form.password.data == 'srvnaeon':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)