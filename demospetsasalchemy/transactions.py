# Database transactions: Sequence of operations performed on the database and served as a single unit of work, i.e it all happens or none of it happens.

from main import User, Preference, engine

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

user = User(
    first_name = 'John',
    last_name = 'Smith',
    email = 'jsmith@hotmail.com'
)

session.add(user)

raise Exception("Something went wrong during session creation")

preference = Preference(
    language = "English",
    currency = "GBP"
)
preference.User = user
session.commit()

