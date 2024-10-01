from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, String, Integer, Float
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin
metadata = MetaData()
# Base = declarative_base
db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model,SerializerMixin):
    __tablename__ = 'earthquakes'

    id=db.Column(db.Integer, primary_key=True)
    magnitude=db.Column(db.Float, nullable=False)
    location=db.Column(db.String, nullable=False)
    year=db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
    