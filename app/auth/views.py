# from flask  import render_template, request, redirect, url_for
from flask  import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from app.models import User
from .forms import LoginForm, ReistrationForm
# from ..import db, main
from ..import db

@auth.route('/login', methods=["POST","GET"])
def login():
    form = LoginForm
    if request.method == "POST":
        form = request.form
        username = form.get("username")
        password = form.get("password")
        email = form.get("email")
        user =  User.query.filter_by(username=username,email=form.email.data).first()
        if user == None:
            error =  "username does not exist"
            return render_template("login.html", error=error)
        is_correct_password = user.check_password(password)
        if is_correct_password==False:
            error =  "Incorrect password"
            return render_template("login.html", error=error)
        login_user(user,form.remember.data)
        return redirect(request.args.get('next') or url_for("main.index"))

    title = "Minute Pitch Login"
    return render_template("auth/login.html",login_form=login_form,title=title)

@auth.route("/sign-up",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        form = request.form 
        username = form.get("username")
        email = form.get("email")
        password =  form.get("password")
        confirm_password =  form.get("confirm_password")
        if username == None or password == None or email==None or confirm_password==None:
            error="username, email and password are required"
            return render_template("signup.html", error=error)
        if password != confirm_password:
            error="Passwords  do not match"
            return render_template("signup.html", error=error)
        else:
            user =  User.query.filter_by(username=username).first()
            if user != None:
                error = "user with that username already exists"
                return render_template("signup.html", error=error)
            user =  User.query.filter_by(email=email).first()
            if user != None:
                error = "user with that email already exists"
                return render_template("signup.html", error=error)

            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect(url_for("auth.login"))
    return render_template("signup.html")


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))