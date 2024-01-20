from tortoise import Tortoise
from settings import DB_URL


async def init_database():
    await Tortoise.init(
        db_url=DB_URL,
        modules={'models': ['db.models', 'aerich.models']}
    ) 
  