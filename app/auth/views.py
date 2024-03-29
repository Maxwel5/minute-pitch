from flask  import render_template, request, redirect, url_for, flash
from ..models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, logout_user, login_required
from . import auth
from app.models import User
from .forms import LoginForm, SignupForm
from ..import db
from ..email import mail_message

@auth.route('/home')
def home():
    return render_template('index.html')

@auth.route('/login', methods=["POST","GET"])
def login():
    form = LoginForm()
    title = "Minute Pitch Login"
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user != None and check_password_hash(user.password,form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for("main.index"))

        flash('Unknown username or password')

    title = 'Login Pitches'

    return render_template("authentication/login.html",login_form=form,title=title)

@auth.route("/sign-up",methods=["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if form.validate_on_submit():
            password_hash=generate_password_hash(form.password.data)
            user=User(email = form.email.data, username = form.username.data, password = password_hash )
            db.session.add(user)
            db.session.commit()
            try:
                mail_message("Welcome to pitches","email/welcome_user",user.email,user=user)
            except Exception:
                print('mail failed')
            return redirect(url_for('auth.login'))
        title = "New Account"


    return render_template("authentication/signup.html", form = form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))