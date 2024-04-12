from models import session, User

#Creating users
user1 = User(username="Zeq Tech 1")
user2 = User(username="Zeq Tech 2")
user3 = User(username="Zeq Tech 3")

#Creating relationships
user1.following.append(user2)
user2.following.append(user3)
user3.following.append(user1)

#Adding users to the session and committing changes to the database
session.add_all([user1, user2, user3])
session.commit()

#return object based on association
print(f"{user1.following = }")
print(f"{user2.following = }")
print(f"{user3.following = }")


