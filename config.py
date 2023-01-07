def load_config():
    return DevConfig()

class Config:
    pass

class DevConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000