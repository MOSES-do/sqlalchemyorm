#sessionmaker is required to create a new record
from sqlalchemy import or_ 
from sqlalchemy import not_ 
from sqlalchemy.orm import sessionmaker 

from models import User, engine

# describes the database where these transactions should be performed
Session = sessionmaker(bind=engine)
session = Session()

#query all users
users_all = session.query(User).all()

#query all users with age greater than or equal to 25
##Implicitly "AND" separates both condition in the filter parentheses
users_filtered = session.query(User).filter(User.age >= 25, User.name == "Iron Man").all()
#len returns number of users
# print("All users:", len(users_all))
# print("Filtered users:", len(users_filtered))

####WHERE#####
users_filtered = session.query(User).where(User.age >= 25).all()
# for user in users_filtered:
#     print(f"User age: {user.age}")


##########OR#################
# users_filtered = session.query(User).where(or_(User.age >= 25, User.name == "Iron Man")).all()
#using Bitwise or operator : |
users_filtered = session.query(User).where((User.age >= 25) | (User.name == "Iron Man")).all()
# for user in users_filtered:
#      print(f"{user.age} - {user.name}")

#_not negation operator
users_filtered = session.query(User).where(not_(User.name == "Iron Man")).all()
# for user in users_filtered:
#      print(f"{user.age} - {user.name}")

