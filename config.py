import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecret")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI", "postgresql://malik1:malik1@localhost:5432/postgres"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
