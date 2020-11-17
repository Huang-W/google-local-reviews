from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path

# DEFAULT_DIR = '/tmp/{}/{}'
# Windows friendly, use local dir
DEFAULT_DIR = 'cli/files/{}__{}__{}'

Base = declarative_base()

def file_loc(context):
    lat = context.get_current_parameters()['lat']
    long = context.get_current_parameters()['long']
    categories = context.get_current_parameters()['categories']
    return DEFAULT_DIR.format(lat, long, categories)

class DataFile(Base):
    __tablename__ = 'data'
    # Unique autoincrement ID
    id = Column(Integer, primary_key=True, nullable=False)
    lat = Column(String, nullable=False)
    long = Column(String, nullable=False)
    categories = Column(String, nullable=False)
    # file location on local system, so that we're not storing large raw data in the DB
    filename = Column(String, nullable=False, default=file_loc)

    def get_file(self, session, lat=None, long=None, categories=None):
        if lat and long and categories:
            ret = session.query(DataFile).filter_by(lat=lat, long=long, categories=categories).first()
        else:
            raise('Both latitude and longitude are needed')

        with open(ret.filename, 'rb') as f:
            data = f.read()

        return data

    def write_file(self, session, contents, lat, long, categories):
        row = DataFile(lat=lat,long=long,categories=categories)
        data_loc = DEFAULT_DIR.format(lat, long, categories)
        session.add(row)

        # Store in local filesystem
        if isinstance(contents, str):
            # print('open w')
            with open(data_loc, 'w') as f:
                f.write(contents)
        elif isinstance(contents, bytes):
            # print('open wb')
            with open(data_loc, 'wb') as f:
                f.write(contents)

        return row

if __name__ == "__main__":
    # Create tables
    engine = create_engine('sqlite:///cli/glocal.db')
    Base.metadata.create_all(engine)

    # Create the session object
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add some test data
    my_data = DataFile(lat='123',long='456',categories='asian-buffet')
    session.add(my_data)
    session.commit()

    # Read the row back
    ret = session.query(DataFile).first()
    print('File {} with lat {} long {} and categories: {}'.format(ret.filename, ret.lat, ret.long, ret.categories))

    # TODO: Username and filename should be inferred from the object
    ret.write_file(session, 'me so tasty', '123', '456', 'asian-buffet')
    session.commit()

    # Read the contents back from the file:
    result = ret.get_file(session, '123', '456', 'asian-buffet')

    # TODO: This is always bytes, maybe we need an indicator of what the file type is.
    print(result)

    session.close()

    # Drop the tables
    Base.metadata.drop_all(engine)
