step 1
install pip istall sqlalchemy

step 2:
create a database engine
/\*\*
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///database.db"
engine = create_engine(db_url)
Base = declarative_base()

# This line creates the database and all of the tables associated with it

Base.metadata.create_all(engine)

run code in vscode using "run" and the databse will be created. In our case database.db
\*/

Step 3:
Install database client by Weijing Chen
to view databse right within VSCODE another alternative is to use mysql workbench

Step 4:
Create databse connection
