from aiogram import Router, F
from aiogram.utils.i18n import gettext as _

from utils import answer_button
from .base import BaseAnonymHandler
from strings import MSG_NEW_VIDEO


router = Router()

@router.message(F.video)
class AnonVideoMessageHandler(BaseAnonymHandler):
    answer_text = _(MSG_NEW_VIDEO)
    content_type = 'video'
    
    async def send(self):
        text = self.event.html_text
        await self.bot.send_video(
            chat_id=self.anon_user.id,
            video=self.event.video.file_id,
            caption=self.answer_text.format(msg=text),
            reply_markup=answer_button(self.from_user.id)
        )
        