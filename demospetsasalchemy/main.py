from datetime import datetime

from sqlalchemy import create_engine, event, Engine, Column, DateTime, String, ForeignKey, String, Integer
from sqlalchemy.orm import declarative_base, Relationship


engine = create_engine(f"sqlite:///database.db", echo=True)

Base = declarative_base()

class TimeStampedModel(Base):
    __abstract__ = True
    
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())


class User(TimeStampedModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(320), nullable=False, unique=True)

    #passive_deletes automatically handles deletion of a relationship if deleted from the parent table
    preference = Relationship("Preference", back_populates="user", uselist=False, passive_deletes=True)
    addresses = Relationship("Address", back_populates="user", passive_deletes=True)

    roles = Relationship("Role", secondary="user_roles", back_populates="users", passive_deletes=True)


    def __repr__(self):
        return f"{self.__class__.__name__}, name:{self.first_name} {self.last_name}"


#one to one relationship
class Preference(TimeStampedModel):
    __tablename__ = 'preferences'

    id = Column(Integer, primary_key=True, autoincrement=True)
    language = Column(String(80), nullable=False)
    currency = Column(String(3), nullable=False)

    #CASCADE: This ensures that when a user with preference is deleted from the User Table,
    #his preference is deleted from the preference table
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True, unique=True)

    user = Relationship("User", back_populates="preference")

    # def __repr__(self):
    #     return f"{self.__class__.__name__} {self.user}"

#one to many relationship
class Address(TimeStampedModel):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    road_name = Column(String(80), nullable=False)
    postcode = Column(String(80), nullable=False)
    city = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)

    user = Relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"{self.__class__.__name__}, name:{self.city} {self.road_name}"


#many to many relationship
class Role(Base):
    __tablename__ = "roles"
        
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    slug = Column(String(80), nullable=False, unique=True)

    users = Relationship("User", secondary="user_roles", back_populates="roles", passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, name:{self.name}"
        

#pivot or associative table
class UserRole(TimeStampedModel):
     __tablename__ = "user_roles"

     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
     role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)
    









# session = scoped_session(
#     sessionmaker(
#         autoflush=False,
#         autocommit=False,
#         bind=engine
#     )
# )

# @event.listens_for(Engine, "connect")
# def set_sqlite_pragma(dbapi_connection, connection_record):
#         cursor = dbapi_connection.cursor()
#         cursor.execute("PRAGMA foreign_keys=ON")
#         cursor.close()

Base.metadata.create_all(engine)
