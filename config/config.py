import os

class Config:
    # 基础配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key_please_change_in_production'
    
    # 数据库配置
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'oracle+cx_oracle://system:12345678@localhost:1531/PRICDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT配置
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt_dev_key_please_change_in_production'
    JWT_ACCESS_TOKEN_EXPIRES = 24 * 60 * 60  # 24 小时

    # 允许的图片类型
    ALLOWED_IMGS = {'bmp', 'png', 'jpg', 'jpeg', 'gif'}
    
    # 图片上传路径
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    IMG_UPLOAD_DIR = os.path.join(STATIC_DIR, 'img')
    
    # 日志监控配置
    LOG_MONITOR_FILE = os.environ.get('LOG_MONITOR_FILE') or '/tmp/test.log'  # 默认监控的日志文件
    LOG_MONITOR_MAX_LINES = int(os.environ.get('LOG_MONITOR_MAX_LINES') or 1000)    # 最大显示行数
    LOG_MONITOR_UPDATE_INTERVAL = int(os.environ.get('LOG_MONITOR_UPDATE_INTERVAL') or 5)  # 更新间隔(秒)
    
    # 确保必要的目录存在
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
    # 测试环境仍使用内存SQLite数据库，便于快速测试
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}