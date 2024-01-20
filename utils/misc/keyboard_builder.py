from aiogram import types
from urllib.parse import quote_plus
from aiogram.utils.i18n import gettext as _
from aiogram.filters.callback_data import CallbackData

from .id_cipher import cipher
from settings import LANGUAGES


class AnswerButton(CallbackData, prefix="answer"):
    ref: str

class LanguageButton(CallbackData, prefix="language"):
    lang: str


def share_button(link: str) -> types.InlineKeyboardMarkup:
    from strings import SHARE_BUTTON_TEXT, BOT_INFO
    share_link = "https://t.me/share/url?url=" + quote_plus(_(BOT_INFO)) + "&text=" + link
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(
                text=_(SHARE_BUTTON_TEXT), url=share_link
            )]
        ]
    )


def answer_button(user_id: int) -> types.InlineKeyboardMarkup:
    from strings import ANSWER_BUTTON_TEXT
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(
                text=_(ANSWER_BUTTON_TEXT),
                callback_data=AnswerButton(ref=cipher(user_id)).pack()
            )]
        ]
    )

langs_keyboard = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(
            text=f"{value} [{name.upper()}]", 
            callback_data=LanguageButton(lang=name).pack()
        )] for name, value in LANGUAGES.items()
    ]
)
