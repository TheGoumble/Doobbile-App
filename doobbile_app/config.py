from doobbile_app.secrets import SECRET_KEY, EMAIL_USER, EMAIL_PASSWORD

class Config:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = EMAIL_USER
    MAIL_PASSWORD = EMAIL_PASSWORD
