from sqlalchemy import (Column, ForeignKey, Integer, String, Text, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload

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
    sensitive_infos = relationship("SensitiveInformation", lazy='raise', backref='user')

    def __repr__(self):
        return f"<User: {self.name}>"

class SensitiveInformation(Base):
    __tablename__ = 'sensitive_information'
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<SensitiveInformation: {self.id}>"

Base.metadata.create_all(engine)

# session.add_all([
#     User(
#         name=f"User {y}",
#         sensitive_infos=[
#             SensitiveInformation(content=f"This is the content for user {y}")
#             for x in range(5)
#         ]
#     ) for y in range(10)
# ])
# session.commit()

#.options(joinedload()): Allows us to specify the relationship to be accessed by our query
#by default we set a flag to raise exception whenevr we try to access the child/related table
users = session.query(User).options(joinedload(User.sensitive_infos)).all()

for user in users:
    print(user.name)
    try:
        for information in user.sensitive_infos: #This will raise an exception
            print(information.content)
    except Exception as e:
        print("Sesnsitive infirmation cannot be accessed directly", e)


