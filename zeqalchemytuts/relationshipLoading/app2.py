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
    posts = relationship("Post", lazy='selectin', backref="user")

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

# session.add_all([
#     User(
#         name=f"User {y}",
#         posts=[
#             Post(content=f"This is the contentfor {y * 5 + x}")
#             for x in range(5)
#         ]
#     ) for y in range(1_000)
# ])
# session.commit()

print('\n Accessing All users posts')

start = perf_counter()
users = session.query(User).all()


for user in users:
    user.posts

print(f"Done in: {perf_counter() - start}")

