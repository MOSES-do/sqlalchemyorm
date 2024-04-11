from models import Address, session, User

#Creating users
user1 = User(name="Jonn Doe", age=52)
user2 = User(name="Jane Doe", age=45)

#Creating addresses
address1 = Address(city="New York", state="NY", zip_code="10001")
address2 = Address(city="Los Angeles", state="CA", zip_code="90001")
address3 = Address(city="Chicago", state="IL", zip_code="60601")

#Associating addresses with users
#he default behaviour of a relationship btw tables in alchemy is a list structure and therefore can use list functions
user1.addresses.extend([address1, address2])
user2.addresses.append(address3)

session.add(user1)
session.add(user2)
session.commit()

#return object based on association
print(f"{user1.addresses = }")
print(f"{user2.addresses = }")
print(f"{address1.user = }")
print(f"{address3.user = }")

