#sessionmaker is required to create a new record
from sqlalchemy.orm import sessionmaker 

from models import User, engine

# describes the database where these transactions should be performed
Session = sessionmaker(bind=engine)

session = Session()

# making entries into database
# user = User(name="John Doe", age=30)
# user_2 = User(name="Andrew Doe", age=30)
# user_3 = User(name="Divine Moses", age=30)
# user_4 = User(name="Esumei Moses", age=30)

# session.add(user_2)
# session.add_all([user_3, user_4])

# session.commit()

# read from database
users = session.query(User).all()

print(users)
print(users)

