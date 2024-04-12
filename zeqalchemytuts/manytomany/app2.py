from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

db_url = "sqlite:///manytomany/database.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

#This enables us to use class as the blueprint for our table
Base = declarative_base()

class UserAssociation(Base):
    __tablename__ = 'user_associations'
    id = Column(Integer, primary_key=True)

    follower_id = Column(Integer, ForeignKey('users.id'))
    following_id = Column(Integer, ForeignKey('users.id'))

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    #
    #access users user is following
    following = relationship("User", 
                             secondary="user_associations",
                             primaryjoin="UserAssociation.follower_id==User.id",
                             secondaryjoin="UserAssociation.following_id==User.id",
                             #access followers to current users
                             backref='followers',
                             )

    def __repr__(self):
        return f'<User: {self.name}>'

Base.metadata.create_all(engine)

user_1 = User(name="John")
user_2 = User(name="Rob")
user_3 = User(name="Kyle")

user_1.following.append(user_2)
user_2.following.append(user_1)
user_3.following.append(user_1)

# session.add_all([user_1, user_2, user_3])
# session.commit()

print(f"{user_1} is following: {user_1.following}")
print(f"{user_1} is being followed by: {user_1.followers}")




