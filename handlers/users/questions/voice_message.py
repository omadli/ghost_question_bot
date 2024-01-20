from aiogram import Router, F
from aiogram.utils.i18n import gettext as _

from utils import answer_button
from .base import BaseAnonymHandler
from strings import MSG_NEW_VOICE


router = Router()

@router.message(F.voice)
class AnonVoiceMessageHandler(BaseAnonymHandler):
    answer_text = _(MSG_NEW_VOICE)
    content_type = 'voice'

    async def send(self):
        text = self.event.html_text
        await self.bot.send_voice(
            chat_id=self.anon_user.id,
            voice=self.event.voice.file_id,
            caption=self.answer_text.format(msg=text),
            reply_markup=answer_button(self.from_user.id)
        )
