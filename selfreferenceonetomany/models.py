#SELF REFERENCE E.G. A USER FOLLOWING ANOTHER USER

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship, sessionmaker

db_url = "sqlite:///selfreferenceonetomany/database.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
#creates session to allow us perform trasactions in our database
session = Session()

#This enables us to use class as the blueprint for our table
Base = declarative_base()

#Some ways to declare relationships in SQL Alchemy
#We will consider mapped and non mapped
class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped = True

    id = Column(Integer, primary_key=True)

class FollowingAssociation(BaseModel):
    __tablename__ = 'following_association'
    user_id = Column(Integer, ForeignKey("users.id"))
    following_id = Column(Integer, ForeignKey("users.id"))

class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String)
    
    #relationship to same table
    #primaryjoin links current user to the association table
    #secondaryjoin links table to the followed user
    #FollowingAssociation.user_id==User.id - checks if user intiating the follower req exists
    #FollowingAssociation.following_id==User.id - checks if user to be followed exists in users table
    following = relationship('User', secondary="following_association",
                             primaryjoin=("FollowingAssociation.user_id==User.id"),
                             secondaryjoin=("FollowingAssociation.following_id==User.id"),
                             )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, following={self.following})>"
    

# This line creates the database and all of the tables associated with it
Base.metadata.create_all(engine)


