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
    posts = relationship("Post", lazy='dynamic', backref='user')

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
        name=f"Zeq",
        posts=[
            Post(content=f"This is the contentfor {x}")
            for x in range(50)
        ]
    )
])
session.commit()

#returns user object
user = session.query(User).filter_by(name='Zeq').first()
print(user.posts)

recent_posts = user.posts.order_by(Post.id.desc()).limit(10).all()
for post in recent_posts:
    print(post.content)


