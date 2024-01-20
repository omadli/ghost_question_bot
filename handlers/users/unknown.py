from aiogram import Router, types, F
from aiogram.utils.i18n import gettext as _

from strings import MSG_HELP
from utils import referal_link


router = Router()

@router.message(F.text)
async def unknown_handler(msg: types.Message):
    await msg.reply(
        text=_(MSG_HELP).format(link=referal_link(msg.from_user.id))
    )
