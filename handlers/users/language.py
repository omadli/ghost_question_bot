from aiogram import types, Router
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _

from db.models import DbUser
from utils import langs_keyboard, LanguageButton
from utils.cache import cache, build_key
from strings import CHANGE_LANGUAGE, LANGUAGE_CHANGED, LANGUAGE_CHANGED_ALERT


router = Router()

@router.message(Command("language"))
async def cmd_language(msg: types.Message):
    await msg.reply(
        text=_(CHANGE_LANGUAGE),
        reply_markup=langs_keyboard,
    )

@router.callback_query(LanguageButton.filter())
async def set_language(call: types.CallbackQuery, callback_data: LanguageButton, db_user: dict):
    dbuser = DbUser(**db_user)
    lang = callback_data.lang
    dbuser.language = lang
    db_user["language"] = lang
    await dbuser.save(update_fields=["language"], force_update=True)
    await cache.delete(build_key(call.from_user.id))
    await call.answer(
        text=_(LANGUAGE_CHANGED_ALERT, locale=lang).format(lang=callback_data.lang),
        show_alert=True
    )
    await call.message.edit_text(
        text=_(LANGUAGE_CHANGED, locale=lang).format(lang=callback_data.lang.upper())
    )
