from asyncpg import UniqueViolationError

from utils.db_api.db_link_2 import db
from utils.db_api.schemas.user import User


async def add_user(id: int, name: str):
    try:
        user = User(id=id, name=name)
        await user.create()
    except UniqueViolationError:
        pass

async def select_all_users():
    users = await User.query.gino.all()
    return users

async def select_user(id:int):
    user = await User.query.where(User.id == id).gino.first()
    return user

async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total

