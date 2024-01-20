from aiogram import Router, F
from aiogram.utils.i18n import gettext as _

from utils import answer_button
from .base import BaseAnonymHandler
from strings import MSG_NEW_PHOTO


router = Router()

@router.message(F.photo)
class AnonPhotoMessageHandler(BaseAnonymHandler):
    answer_text = _(MSG_NEW_PHOTO)
    content_type = 'photo'
    
    async def send(self):
        text = self.event.html_text
        await self.bot.send_photo(
            chat_id=self.anon_user.id,
            photo=self.event.photo[-1].file_id,
            caption=self.answer_text.format(msg=text),
            reply_markup=answer_button(self.from_user.id)
        )
