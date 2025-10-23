from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

database = SQLAlchemy()

# Class to register users
class Register():
    def __init__(self):
        self.id = Column(Integer, primary_key=True)
        self.username = Column(String(50), unique=True, nullable=False)
        self.email = Column(String(120), unique=True, nullable=False)
        self.password = Column(String(128), nullable=False)

    __tablename__ = "users_registers"
