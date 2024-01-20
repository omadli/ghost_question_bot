from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _

from strings import MSG_ABOUT

router = Router()

@router.message(Command("about"))
async def cmd_help(msg: types.Message):
    await msg.reply(
        text=_(MSG_ABOUT)
    )
