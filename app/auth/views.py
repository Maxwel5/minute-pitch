# from flask  import render_template, request, redirect, url_for
from flask  import render_template, request, redirect, url_for, flash
from ..models import User
from flask_login import login_user, logout_user, login_required
from . import auth
from app.models import User
from .forms import LoginForm, SignupForm
# from ..import db, main
from ..import db
# from werkzeug.security import generate_password_hash,check_password_hash

# @auth.route('/')
@auth.route('/home')
def home():
    return render_template('index.html')

@auth.route('/login', methods=["POST","GET"])
def login():
    form = LoginForm()
    title = "Minute Pitch Login"
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user != None and form.password.data == user.password:
            login_user(user)
            return redirect(request.args.get('next') or url_for("main.index"))
        else:
            return render_template("authentication/login.html",login_form=form,title=title)

    return render_template("authentication/login.html",login_form=form,title=title)

@auth.route("/sign-up",methods=["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        # username = form.username.data
        # email = form.email.data

        # user = User(username = username,email = email)
        # user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

    return render_template("authentication/signup.html", form = form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))