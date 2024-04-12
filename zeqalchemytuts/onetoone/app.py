from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = 'sqlite:///onetoone/database.db'

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
#creates session to allow us perform trasactions in our database
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship("Address", back_populates="user", uselist=False)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="address")

Base.metadata.create_all(engine)

new_user = User(name='John Doe')
new_address = Address(email='john@example.com', user=new_user)
session.add_all([new_user, new_address])
session.commit()

