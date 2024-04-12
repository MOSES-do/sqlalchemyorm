from sqlalchemy import (Column, ForeignKey, Integer, String, Text, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = 'sqlite:///relationshipLoading/database.db'

engine = create_engine(db_url, echo=True) #important

Session = sessionmaker(bind=engine)
#creates session to allow us perform trasactions in our database
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship("Post", lazy='select', backref="user")

    def __repr__(self):
        return f"<User: {self.name}>"

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Post: {self.id}>"

Base.metadata.create_all(engine)

new_user = User(
    name="Bob",
    posts=[
        Post(content=f"This is the content for {x}")
            #list comprehension/generate 4 posts for the user
             for x in range(1, 5)
    ]
)
session.add_all([new_user])
session.commit()

user = session.query(User).first()

print('Accessing user')
print(user)
print('Accessing posts specifically')
print(user.posts)

