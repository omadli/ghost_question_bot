from aiogram.utils.i18n import I18n
from aiogram import Dispatcher, Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from settings import BOT_TOKEN, USE_REDIS, DEFAULT_LANGUAGE


storage = MemoryStorage()

if USE_REDIS:
    from settings import REDIS_DB, REDIS_PASSWORD
    from aiogram.fsm.storage.redis import Redis, RedisStorage
    
    redis_client = Redis(db=REDIS_DB, password=REDIS_PASSWORD)
    storage = RedisStorage(redis_client, data_ttl=2*60*60) # 2 hour
    
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(
    storage=storage
)
i18n = I18n(path="locales", default_locale=DEFAULT_LANGUAGE, domain="messages")
