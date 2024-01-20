from aiogram import Router, F
from aiogram.utils.i18n import gettext as _

from utils import answer_button
from .base import BaseAnonymHandler
from strings import MSG_NEW_AUDIO


router = Router()

@router.message(F.audio)
class AnonAudioMessageHandler(BaseAnonymHandler):
    answer_text = _(MSG_NEW_AUDIO)
    content_type = 'text'

    async def send(self):
        text = self.event.html_text
        await self.bot.send_audio(
            chat_id=self.anon_user.id,
            audio=self.event.audio.file_id,
            caption=self.answer_text.format(msg=text),
            reply_markup=answer_button(self.from_user.id)
        )
