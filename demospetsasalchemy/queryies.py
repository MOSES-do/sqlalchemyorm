from sqlalchemy.orm import sessionmaker 

from main import User, engine, Preference, Address, Role 

Session = sessionmaker(bind=engine)

session = Session()

all_users = session.query(User).all()
gmail_users = session.query(User).filter(User.email.like("%@gmail.com")).all()
# print(all_users)
# print(gmail_users)

# joins
super_admins = (
    session.query(User)
    .join(User.roles)
    .filter(Role.slug == "super-admin")
    .all()
)
# print(super_admins)

# order_by
users_by_name = session.query(User).order_by(User.first_name.asc()).all()
# print(users_by_name)
# for user in users_by_name:
#         print(f"User id: {user.id}, name: {user.first_name}, email: {user.email}")


#limit query result
first_three_users = session.query(User).limit(3).all()
# print(first_three_users)

# offset
skip_three_users = session.query(User).offset(3).all()
# print(skip_three_users)

num_of_users = session.query(User).count()
print(num_of_users)