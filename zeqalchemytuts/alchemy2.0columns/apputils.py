from sqlalchemy import ForeignKey, create_engine, select
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker, relationship

from utils import str_20, str_100

db_url = "sqlite:///alchemy2.0columns/database1.db"
engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)
#creates session to allow us perform trasactions in our database
session = Session()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str_20]
    last_name: Mapped[str_100]
    posts: Mapped[list["Post"]] = relationship()

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    content: Mapped[str]

    def __repr__(self):
        return f"<Post: {self.content}>"


# This line creates the database and all of the tables associated with it
Base.metadata.create_all(engine)

# user = User(first_name='ace.io', last_name='technologies', posts=[Post(content="This is some work bro")])
# session.add(user)
# session.commit()

user = session.scalar(select(User))
print(f"\nUser {user.id}: {user.first_name} {user.last_name} {user.posts} \n")

user = session.query(User).first()
print(f"\nUser {user.id}: {user.first_name} {user.last_name} {user.posts} \n")






























# type_map: Dict[Type[Any], TypeEngine[Any]] = {
#     bool: types.Boolean(),
#     bytes: types.LargeBinary(),
#     datetime.date: types.Date(),
#     datetime.datetime: types.Datetime(),
#     datetime.time: types.Time(),
#     decimal: types.Boolean(),
#     float: types.Float(),
#     int: types.Integer(),
#     str: types.String(),
#     uuid.UUID: types.Uuid()(),
# }