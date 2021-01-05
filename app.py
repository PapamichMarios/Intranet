from sqlalchemy import create_engine
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/intranet"

# SQL Alchemy
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# import models
from model import User

Base.metadata.create_all(bind=engine)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
