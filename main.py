import asyncio
import logging

from loader import bot, dp
from utils.startup import on_startup
from handlers import include_all_routers

include_all_routers(dp)


async def main():
    await on_startup(dp, bot)
    logging.info("Bot started")
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped by user")
    except Exception as e:
        logging.info("Bot stopped by: ", e)
