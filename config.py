class BaseConfig:
    "Base config class"
    SECRET_KEY = 'asecretkey'
    DEBUG = True


class ProductionConfig(BaseConfig):
    "Production config"
    SECRET_KEY = 'asecretkey'
    DEBUG = False

