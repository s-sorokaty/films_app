from sqlalchemy import create_engine


from settings import get_settings


settings = get_settings()

db_connect_key = settings.MYSQL_USER + ':' + settings.MYSQL_PASSWORD + '@' + \
    settings.MYSQL_HOST + ':' + \
    str(settings.MYSQL_PORT) + '/' + settings.MYSQL_DATABASE + '?charset=utf8mb4'
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://" + db_connect_key

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    convert_unicode=True
)
