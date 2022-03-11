import sqlalchemy as db
from helpers.secret import config

# specify database configurations


db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

# specify connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

# connect to database
engine = db.create_engine(connection_str)


# pull metadata of a table
metadata = db.MetaData(bind=engine)
metadata.reflect(only=['drafts'])

test_table = metadata.tables



