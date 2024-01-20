from aiogram import Router, F
from aiogram.utils.i18n import gettext as _

from utils import answer_button
from .base import BaseAnonymHandler
from strings import MSG_NEW_QUESTION


router = Router()

@router.message(F.text)
class AnonTextMessageHandler(BaseAnonymHandler):
    answer_text = _(MSG_NEW_QUESTION)
    content_type = 'text'
    
    async def send(self):
        text = self.event.html_text
        await self.bot.send_message(
            chat_id=self.anon_user.id,
            text=self.answer_text.format(msg=text),
            reply_markup=answer_button(self.from_user.id)
        )
    