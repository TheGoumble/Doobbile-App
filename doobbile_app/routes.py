from flask import render_template, url_for, flash, redirect
from doobbile_app import app
from doobbile_app.forms import RegistrationForm, LoginForm
from doobbile_app.models import User, Post

posts = [
    {
        "author": "Javier Vargas",
        "title": "Doobbile Post 1",
        "content": "This would be the SVG",
        "caption": "This is my drawing",
        "date_posted": "March 31, 2018"
    },
    {
        "author": "John Mackland",
        "title": "Doobbile Post 2",
        "content": "This would be the SVG",
        "caption": "This is my animal drawing",
        "date_posted": "March 31, 2018"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@doobbile.com' and form.password.data == 'password':
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and passwrod", "danger")
    return render_template('login.html', title="Login", form=form)
