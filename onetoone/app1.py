from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = 'sqlite:///onetoone/database1.db'

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
#creates session to allow us perform trasactions in our database
session = Session()

Base = declarative_base()

class Node(Base):
    __tablename__ = 'nodes'
    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Node value={self.value}>"
    
    #A circular dependemncy problem arises from doing this it's recomended to use an association table
    node_id = Column(Integer, ForeignKey('nodes.id'))
    next_node = relationship("Node", remote_side=[id], uselist=False)

Base.metadata.create_all(engine)

node1 = Node(value=1)
node2 = Node(value=2)
node3 = Node(value=3)

#linked list kinda one to one relationship
node1.next_node = node2
node2.next_node = node3
node2.next_node = node1

session.add_all([node1, node2, node3])
session.commit()

