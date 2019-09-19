# from flask  import render_template, request, redirect, url_for
from flask  import render_template, request, redirect, url_for, flash
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
            

            
            
    # if request.method == "POST":
    #     form = request.form
    #     username = form.get("username")
    #     password = form.get("password")
    #     user =  User.query.filter_by(username=username).first()
    #     if user == None:
    #         error =  "username does not exist"
    #         return render_template("authentication/login.html", error=error)
    #     is_correct_password = user.check_password(password)
    #     if is_correct_password==False:
    #         error =  "Incorrect password"
    #         return render_template("authentication/login.html", error=error)
    #     login_user(user,form.remember.data)
    #     return redirect(request.args.get('next') or url_for("main.index"))

    
    return render_template("authentication/login.html",login_form=form,title=title)

@auth.route("/sign-up",methods=["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        user = User(username = username,email = email)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

    # if request.method == "POST":
    #     form = request.form 
    #     username = form.get("username")
    #     email = form.get("email")
    #     password =  form.get("password")
    #     confirm_password =  form.get("confirm_password")
    #     if username == None or password == None or email==None or confirm_password==None:
    #         error="username, email and password are required"
    #         return render_template("authenticate/signup.html", error=error)
    #     if password != confirm_password:
    #         error="Passwords  do not match"
    #         return render_template("authenticate/signup.html", error=error)
    #     else:
    #         user =  User.query.filter_by(username=username).first()
    #         if user != None:
    #             error = "user with that username already exists"
    #             return render_template("authenticate/signup.html", error=error)
    #         user =  User.query.filter_by(email=email).first()
    #         if user != None:
    #             error = "user with that email already exists"
    #             return render_template("authenticate/signup.html", error=error)

    #         user = User(username=username, email=email)
    #         user.set_password(password)
    #         user.save()
    #         return redirect(url_for("auth.login"))
    return render_template("authentication/signup.html", form = form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))