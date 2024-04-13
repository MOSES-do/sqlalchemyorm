from main import User, Address, engine

from sqlalchemy.orm import sessionmaker, joinedload, subqueryload, contains_eager

Session = sessionmaker(bind=engine)

session = Session()

# Eager loading is defined as loading related records with the main records
#Remember there is a relationship between a main table and other tables in a main table
#E.g User table has a relatinship with addresses table defined by using addresses=Relationship("Address", back_populates="users")
#Eager loading allows us direct access to the defined relationship values directly thruogh the main table

# users = (
#     session.query(User)
#     .options(joinedload(User.addresses))
#     .all()
# )


#using a subquery
# users = (
#     session.query(User)
#     .options(subqueryload(User.addresses))
#     .all()
# )

users = (
    session.query(User)
    .join(User.addresses)
    .filter(Address.city == "London")
    .options(contains_eager(User.addresses))
    .all()
)

for user in users:
    print(user.addresses)


