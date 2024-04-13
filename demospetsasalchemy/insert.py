from main import User, Role, Address, Preference, engine

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

admin_role = session.query(Role).filter(Role.slug == "admin").first()

user = User(first_name="Moses", last_name="Esumei", email="archer.me24@gmail.com")
user.roles.append(admin_role)
user.addresses.append(
    Address(road_name="789 Oak St", postcode="54321", city="Paris")
)
user.preference = Preference(
    language="English",
    currency="USD",
)

session.add(user)
session.commit()
print(user)

