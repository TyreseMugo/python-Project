from sqlalchemy import create_engine
# from students import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///class_management_database.db')
session = sessionmaker (bind=engine)
session = session()

convention = {
    "fk":"fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"

}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

