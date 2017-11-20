from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# 注意这里不再传入 app 了
db = SQLAlchemy()

#用户表
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)


#职位表
class Position(db.Model):
    __tablename__ = 'position'

    id = db.Column(db.Integer, primary_key=True)

#公司表
class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
