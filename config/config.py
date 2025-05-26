import os

class Config:
    # Basic configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key_please_change_in_production'
    
    # Database configuration
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'oracle+cx_oracle://system:12345678@localhost:1531/PRICDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT configuration
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt_dev_key_please_change_in_production'
    JWT_ACCESS_TOKEN_EXPIRES = 24 * 60 * 60  # 24 hours

    # Allowed image types
    ALLOWED_IMGS = {'bmp', 'png', 'jpg', 'jpeg', 'gif'}
    
    # Image upload path
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    IMG_UPLOAD_DIR = os.path.join(STATIC_DIR, 'img')
    
    # Log monitoring configuration
    LOG_MONITOR_FILE = os.environ.get('LOG_MONITOR_FILE') or '/tmp/test.log'  # Default log file to monitor
    LOG_MONITOR_MAX_LINES = int(os.environ.get('LOG_MONITOR_MAX_LINES') or 1000)    # Maximum lines to display
    LOG_MONITOR_UPDATE_INTERVAL = int(os.environ.get('LOG_MONITOR_UPDATE_INTERVAL') or 5)  # Update interval (seconds)
    
    # Ensure required directories exist
    @staticmethod
    def init_app(app):
        os.makedirs(Config.STATIC_DIR, exist_ok=True)
        os.makedirs(Config.IMG_UPLOAD_DIR, exist_ok=True)

class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    # Testing environment still uses SQLite in-memory database for fast testing
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}