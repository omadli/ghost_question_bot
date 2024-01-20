from aiogram import Router, types, F
from datetime import datetime, timedelta
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _
from aiogram.filters import CommandStart, CommandObject, StateFilter

from db.models import DbUser
from utils import decipher, share_button, referal_link
from strings import MSG_START, MSG_WRITE_QUESTION, MSG_INVALID_REFERAL_LINK


router = Router()


@router.message(CommandStart(deep_link=False, magic= (F.text=='/start')))
async def cmd_start(msg: types.Message):
    link = referal_link(msg.from_user.id)
    mention = msg.from_user.mention_html()
    
    await msg.reply(
        text=_(MSG_START).format(mention=mention, link=link),
        reply_markup=share_button(link)
    )


@router.message(CommandStart(deep_link=True), StateFilter(None, "anonchat"))  
async def cmd_start_chat_in_state(msg: types.Message, command: CommandObject, state: FSMContext, db_user: dict):
    arg = command.args
    anon_user_id = decipher(arg)
    anon_user: DbUser = await DbUser.filter(id=anon_user_id).first()
    if anon_user is None or not anon_user.is_active: # not found or inactive user:
        await msg.reply(_(MSG_INVALID_REFERAL_LINK))
        await state.clear()
        return
    
    user = DbUser(**db_user)
    delta: timedelta = datetime.utcnow() - user.join_date.replace(tzinfo=None)
    if delta.seconds < 10:
        # greeting
        link = referal_link(msg.from_user.id)
        mention = msg.from_user.mention_html()
        
        await msg.reply(
            text=_(MSG_START).format(mention=mention, link=link),
            reply_markup=share_button(link)
        )
        
    await state.set_state("anonchat")
    await state.set_data({"id": anon_user_id, "anon_user": dict(anon_user)})
    await msg.reply(
        text=_(MSG_WRITE_QUESTION),
        reply_markup=types.ForceReply()
    )
