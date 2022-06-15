class BaseConfig:
    DEBUG = False
    FLASK_ENV = 'production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://pg:password@localhost/kilid?sslmode=disable'

