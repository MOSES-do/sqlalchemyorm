#GROUPING AND CHAINING

#sessionmaker is required to create a new record
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import func 

from models import User, engine

# describes the database where these transactions should be performed
Session = sessionmaker(bind=engine)
session = Session()

#query all users
#SQL EQUIVALENT: SELECT age FROM users GROUP BY age;
users = session.query(User.age, func.count(User.id)).group_by(User.age).all()
#returns a tuple of age groups and the number of persons in each group
# print(users)


#SQL EQUIVALENT: SELECT age, COUNT(id) 
                # FROM users WHERE age > 24 AND age < 50
                # GROUP BY age
                # ORDER BY "age"
users_tuple = (
    session.query(User.age, func.count(User.id))
    .filter(User.age > 24)
    .order_by(User.age)
    .filter(User.age < 50)
    .group_by(User.age)
    .all()
)
# for age, count in users_tuple:
#     print(f"Age{age}: {count} users")

only_iron_man = True
group_by_age = True
users = session.query(User)

if only_iron_man:
        users = users.filter(User.name == "Iron Man")

if group_by_age:
        users = users.group_by(User.age)

users = users.all()

for user in users:
        print(f"{user.age} - {user.name}")




