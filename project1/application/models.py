from datetime import datetime
from application import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
   # posts = db.relationship('Review', backref='author', lazy=True)


    def __repr__(self):
        return "User('{}', '{}', '{}', '{}')".format(self.id, self.username, self.email, self.password)


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    book_id = db.Column(db.String, db.ForeignKey('books.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=True)
   # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return "Post('{}', '{}', '{}')".format(self.date_posted, self.book_id, self.rating)

class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer)
    isbn = db.Column(db.String, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    def  __repr__(self):
        return "Books('{}', '{}', '{}', '{}')".format(self.isbn, self.title, self.author, self.year)


