from sqlalchemy import BigInteger, SmallInteger, String
from sqlalchemy.orm import mapped_column
from typing import Optional
from typing_extensions import Annotated


str_20 = Annotated[str, mapped_column(String(20))]
str_50 = Annotated[str, mapped_column(String(50))]
str_70 = Annotated[str, mapped_column(String(70))]
# str_70 = Annotated[String(70), mapped_column()]
str_100 = Annotated[Optional[str], mapped_column(String(100))]

int_small = Annotated[SmallInteger, mapped_column(SmallInteger)]
int_big = Annotated[BigInteger, mapped_column(BigInteger)]
