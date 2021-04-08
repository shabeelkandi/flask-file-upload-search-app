from db_handler import db
from flask_sqlalchemy import SQLAlchemy
import datetime


class files(db.Model):
    id = db.Column("file_id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(200))
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.created_date = datetime.datetime.now()
