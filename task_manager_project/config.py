import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "gizli_anahtar"
    SQLALCHEMY_DATABASE_URI = "sqlite:///tasks.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
