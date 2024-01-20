from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from db.models import DbUser
from utils import decipher, AnswerButton
from strings import MSG_SOMETHING_WENT_WRONG, MSG_WRITE_ANSWER


router = Router()

@router.callback_query(AnswerButton.filter())
async def answer_button_handler(call: types.CallbackQuery, callback_data: AnswerButton, state: FSMContext):
    ref = callback_data.ref
    anon_user_id = decipher(ref)
    anon_user: DbUser = await DbUser.filter(id=anon_user_id).first()
    if anon_user is None or not anon_user.is_active: # not found or inactive user
        await call.message.reply(_(MSG_SOMETHING_WENT_WRONG))
        await state.clear()
        return
    await state.set_state("anonchat")
    await state.set_data({"id": anon_user_id, "anon_user": dict(anon_user)})
    await call.message.reply(
        text=_(MSG_WRITE_ANSWER),
        reply_markup=types.ForceReply()
    )
