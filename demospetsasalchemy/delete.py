from main import User, engine

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

user = session.query(User).first()

session.delete(user)
session.commit()
