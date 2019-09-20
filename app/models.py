from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import db, login_manager

class User(UserMixin, db.Model):
    __tablename__="users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index = True, nullable=False, unique=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255), index = True, nullable=False, unique=True)
    pass_secure = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    # password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(4800))
    profile_pic_path = db.Column(db.String)
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self, password):
        password_hash= generate_password_hash(password)
        self.password=password

    def check_password(self,password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'user: (self.username)'

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    pitch_title = db.Column(db.String(255))
    pitch_content = db.Column(db.String(800))
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)

    comments = db.relationship('Comment',backref =  'pitch_id',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('The password attribute cannot be read')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches

    @classmethod
    def get_pitch(cls,id):
        pitch = Pitch.query.filter_by(id=id).first()

        return pitch

    @classmethod
    def count_pitches(cls,username):
        user = User.query.filter_by(username=username).first()
        pitches = Pitch.query.filter_by(user_id=user.id).all()

        pitches_count = 0
        for pitch in pitches:
            pitches_count += 1

        return pitches_count

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(800))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch):
        comments = Comment.query.filter_by(pitch_id=pitch).all()
        
        return comments