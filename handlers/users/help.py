from aiogram import Router, types, F
from aiogram.utils.i18n import gettext as _
from aiogram.filters import Command, CommandStart

from strings import MSG_HELP
from utils import referal_link


router = Router()


@router.message(Command("help"))
@router.message(CommandStart(deep_link=True), F.text.endswith("help"))
async def cmd_help(msg: types.Message):
    await msg.reply(
        text=_(MSG_HELP).format(link=referal_link(msg.from_user.id))
    )
