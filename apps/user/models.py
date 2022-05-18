from datetime import datetime

from exts import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    username = db.Column(db.String(15),nullable=False)
    password = db.Column(db.String(32),nullable=False)
    phone = db.Column(db.String(11),nullable=False,unique=True)
    email = db.Column(db.String(30))
    icon = db.Column(db.String(100))
    role = db.Column(db.Enum('admin','NJFuser','supplier'))
    isdelete = db.Column(db.Boolean,default=False)
    rdatetime = db.Column(db.DateTime,default=datetime.now)


    def __str__(self):
        return self.username
