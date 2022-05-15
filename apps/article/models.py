from datetime import datetime

from exts import db


class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text,nullable=False)
    pdatetime = db.Column(db.DateTime,default=datetime.now)
    click_num = db.Column(db.Integer,default=0)
    save_num = db.Column(db.Integer,default=0)
    love_num = db.Column(db.Integer,default=0)
    isdelete = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    type_id = db.Column(db.String(20),db.ForeignKey('typeclass.id'))
    comments = db.relationship('Comment',backref='article')

class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    comment = db.Column(db.String(255),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    article_id = db.Column(db.Integer,db.ForeignKey('article.id'))
    cdatetime = db.Column(db.DateTime,default=datetime.now)

    def __str__(self):
        return self.comment

class Typeclass(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    typename = db.Column(db.String(20),nullable=False)
    articles = db.relationship('Article',backref='typeclass')

    def __str__(self):
        return self.typename

