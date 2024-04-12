from sqlalchemy import (Column, ForeignKey, Integer, String, Text, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from time import perf_counter

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
    posts = relationship("Post", lazy='subquery', backref='user')

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

session.add_all([
    User(
        name=f"User {y}",
        posts=[
            Post(content=f"This is the contentfor {y}")
            for x in range(5)
        ]
    ) for y in range(10)
])
session.commit()

users = session.query(User).all()

for user in users:
    print(user.name)
    for post in user.posts:
        print(post.content)


