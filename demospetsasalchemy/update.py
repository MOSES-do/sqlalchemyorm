from main import User, Preference, engine

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

user_preference = (
    session.query(Preference)
    .join(Preference.user)
    .filter(User.email == "archer.me24@gmail.com")
    .first()
    )
print(user_preference)

# update
user_preference.currency = "GBP"
session.commit()

user = session.query(User) \
        .filter(User.first_name == 'John') \
        .filter(User.last_name == 'Doe') \
        .update({"email": "johndoe@ymail.com"})
session.commit()

