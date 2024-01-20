from aiogram import Bot, Router, types
from aiogram.filters import CommandStart
from aiogram.utils.i18n import gettext as _

from strings import MSG_GROUP_START

router = Router()

@router.message(CommandStart())
async def cmd_start(msg: types.Message, bot: Bot):
    me = bot._me
    me_username = me.username
    mention = msg.from_user.mention_html()
    await msg.reply(
        text=_(MSG_GROUP_START).format(mention=mention, me_username=me_username)
    )
