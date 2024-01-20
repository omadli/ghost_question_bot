from typing import Any, Dict
from aiogram.types import TelegramObject
from aiogram.utils.i18n import I18nMiddleware

from settings import DEFAULT_LANGUAGE


class MyI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        db_user: dict = data.get("db_user")
        print("i18n", db_user)
        if db_user is None:
            return DEFAULT_LANGUAGE
        return db_user.get("language", DEFAULT_LANGUAGE)
   