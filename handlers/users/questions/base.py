import logging
from aiogram.fsm.context import FSMContext
from aiogram.handlers import MessageHandler
from aiogram.utils.i18n import gettext as _

from db.models import DbUser
from settings import LOGS_CHANNEL
from utils import referal_link, share_button, answer_button
from strings import MSG_SENT, MSG_SOMETHING_WENT_WRONG


class BaseAnonymHandler(MessageHandler):
    answer_text: str
    content_type: str
    
    async def log_message(self):
        anon_user = self.anon_user
        current_user = self.from_user
        mention1 = "@" + current_user.username if current_user.username else current_user.mention_html()
        mention2 = "@" + anon_user.username if anon_user.username else anon_user.html_mention()
        
        await self.bot.send_message(
            chat_id=LOGS_CHANNEL,
            text=f"Anonym message was sent.\n"
                f"From {mention1} [<code>{current_user.id}</code>] "
                f"to {mention2} [<code>{anon_user.id}</code>]\n"
                f"Content_type: {self.content_type}"
        )
    
    async def send(self):
        caption = self.event.html_text
        await self.event.copy_to(
            chat_id=self.anon_user.id,
            caption=self.answer_text.format(msg=caption),
            reply_markup=answer_button(self.from_user.id),
        )  

    async def handle(self):
        await self.pre_handle()
        try:
            await self.send()
        except Exception as e:
            await self.event.reply(_(MSG_SOMETHING_WENT_WRONG))
            logging.debug("Nimadir xato ketti" + str(e))
            return
        
        await self.post_handle()
        await self.log_message()
        
      
    async def pre_handle(self):
        state: FSMContext = self.data.get('state')
        data = await state.get_data()
        
        anon_user = DbUser(**data.get("anon_user"))
        self.anon_user = anon_user
        

    async def post_handle(self):
        link = referal_link(self.from_user.id)
        await self.event.reply(
            text=_(MSG_SENT).format(link=link),
            reply_markup=share_button(link)
        )
    