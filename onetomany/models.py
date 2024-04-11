from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///onetomany/database.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

#This enables us to use class as the blueprint for our table
Base = declarative_base()

#Some ways to declare relationships in SQL Alchemy
#We will consider mapped and non mapped

#Non-Mapped
class BaseModel(Base):
    #Allows for other classes to inherit from the BASE model
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)

class Address(BaseModel):
    __tablename__ = 'addresses'

    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    #users.id is made up if the table name + column
    user_id = Column(ForeignKey("users.id"))
    #return user associated to an address
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"<Address(id={self.id}, city={self.city})>"

class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String)
    age = Column(Integer)
    #This sets the relationship such that a user can have multiple addresses
    #return Address associated to a user
    addresses = relationship(Address)
    
    def __repr__(self):
        return f"<User(id={self.id}, username={self.name})>"
    

# This line creates the database and all of the tables associated with it
Base.metadata.create_all(engine)


