import random

#sessionmaker is required to create a new record
from sqlalchemy.orm import sessionmaker 

from models import User, engine

# describes the database where these transactions should be performed
Session = sessionmaker(bind=engine)

session = Session()

names = ["Andrew Pip", "Iron Man", "John DOe", "Jane Doe"]
age = [20,21, 22, 23, 25, 27, 30, 35, 60]

for x in range(20):
        user = User(name=random.choice(names), age=random.choice(age))
        # session.add(user)

        # session.commit()


#query table ordered by age (ascending)
users = session.query(User).order_by(User.age.desc(), User.name).all()
# SQL EQUIVALENT: SELECT * FROM users ORDER BY age, name;
# for user in users:
        #  print(f"User id: {user.id}, name: {user.name}, age: {user.age}")
