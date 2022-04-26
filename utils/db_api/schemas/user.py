from sqlalchemy import BigInteger, Column, String, sql

from utils.db_api.db_link_2 import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    query: sql.Select
