from aiogram import Bot, Dispatcher

from .logger import set_logger
from .database_conn import init_database
from .notify_admins import startup_notify
from .bot_commands import set_bot_commands


async def on_startup(dp: Dispatcher, bot: Bot):
    set_logger(dp)
    await init_database()
    await startup_notify(bot)
    await set_bot_commands(bot)
