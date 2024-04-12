from sqlalchemy import BIGINT, SMALLINT, String, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, registry
from typing import Optional
from typing_extensions import Annotated

db_url = "sqlite:///alchemy2.0columns/database.db"
engine = create_engine(db_url, echo=True)

str_20 = Annotated[str, 20]
str_100 = Annotated[str, 100]

class Base(DeclarativeBase):
    # type_annotation_map = {
    #     int: BIGINT,
    # }

    registry = registry(
        type_annotation_map= {
            str_20: String(20),
            str_100: String(100),
        }
    )

class UserLegacy(Base):
    __tablename__ = "users"

    # id = mapped_column(Integer, primary_key=True)
    # name = mapped_column(String)
    # age = mapped_column(Integer)

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[Optional[str_20]] = mapped_column() #allows field to be set to null optionally
    last_name: Mapped[Optional[str_100]]  #allows field to be set to null optionally
    age: Mapped[int] = mapped_column(nullable=True) #allows field to be set to null optionally

# This line creates the database and all of the tables associated with it
Base.metadata.create_all(engine)





























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