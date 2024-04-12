#sessionmaker is required to create a new record
from sqlalchemy.orm import sessionmaker 

from models import User, engine

# describes the database where these transactions should be performed
Session = sessionmaker(bind=engine)
#creates session to allow us perform trasactions in our database
session = Session()

##############CREATE######################
# making entries into database
# user = User(name="John Doe", age=30)
# user_2 = User(name="Andrew Doe", age=30)
# user_3 = User(name="Divine Moses", age=30)
# user_4 = User(name="Esumei Moses", age=30)

# session.add(user_2)
# session.add_all([user_3, user_4])

# session.commit()

################READ from database##############################
# users = session.query(User).all()
# for user in users:
#         print(f"User id: {user.id}, name: {user.name}, age: {user.age}")



################FILTER_BY#################
# .all() | returns an array of the filtered user
# user = session.query(User).filter_by(id=1).all()
# print(user[0])
# print(f"User id: {user[0].id}, name: {user[0].name}, age: {user[0].age}")

# .one_or_none() | returns an object of the filtered user
user = session.query(User).filter_by(id=1).one_or_none()
# print(user)
# print(f"User id: {user.id}, name: {user.name}, age: {user.age}")

# .first() | returns the first occurrence of an object
# user = session.query(User).filter_by(age=30).first()
# print(user)
# print(f"User id: {user.id}, name: {user.name}, age: {user.age}")

###############UPDATE#####################
#Update the user with the id:1
user.name = "Bella Amigos"
session.commit()


###############DELETE#####################
#Update the user with the id:1
session.delete(user)
session.commit()

