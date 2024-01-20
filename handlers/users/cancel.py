from aiogram import Router, types
from aiogram.utils.i18n import gettext as _
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter

from utils import share_button, referal_link
from strings import MSG_CANCEL, MSG_CANCEL_NONE


router = Router()

@router.message(Command("cancel"), StateFilter("anonchat"))  
async def cmd_cancel(msg: types.Message, state: FSMContext):
    await state.clear()
    link = referal_link(msg.from_user.id)
    await msg.reply(
        text=_(MSG_CANCEL).format(link=link),
        reply_markup=share_button(link=link)
    )
    
    
@router.message(Command("cancel"), StateFilter(None))  
async def cmd_cancel_none(msg: types.Message, state: FSMContext):
    await state.clear()
    link = referal_link(msg.from_user.id)
    await msg.reply(
        text=_(MSG_CANCEL_NONE).format(link=link),
        reply_markup=share_button(link=link)
    )
