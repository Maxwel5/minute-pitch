from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import db, login_manager

class User(UserMixin, db.Model):
    __tablename__="users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    firstname = db.Column(db.String(255), nullable=False, unique=True)
    lastname = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(4800))
    profile_pic_path = db.Column(db.String)
    pitch = db.relationship('Pitches', backref='author', lazy='dynamic')
    comments = db.relationship('Comments', backref='author', lazy='dynamic'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self, password):
        password_hash= generate_password_hash(password)
        self.password=pass_hash

    def check_password(self,password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'user: (self.username)'

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)