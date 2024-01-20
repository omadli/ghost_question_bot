import logging
from typing import List
from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _
from aiogram.enums.content_type import ContentType
from aiogram_media_group import media_group_handler

from db.models import DbUser
from settings import LOGS_CHANNEL
from utils import referal_link, share_button, answer_button
from strings import MSG_NEW_QUESTION, MSG_SOMETHING_WENT_WRONG, MSG_SENT


router = Router()

@router.message(F.media_group_id)
@media_group_handler
async def media_group_handler(messages: List[types.Message], state: FSMContext, bot: Bot):
    data = await state.get_data()
    anon_user = DbUser(**data.get("anon_user"))
    
    anon_user = anon_user
    current_user = messages[0].from_user
    
    try:
        medias: List[types.InputMedia] = []
        for m in messages:
            if m.content_type == ContentType.PHOTO:
                medias.append(
                    types.InputMediaPhoto(
                        media=m.photo[-1].file_id,
                        caption=m.html_text
                    )
                )
            elif m.content_type == ContentType.VIDEO:
                medias.append(
                    types.InputMediaVideo(
                        media=m.video.file_id,
                        caption=m.html_text
                    )
                )    
            elif m.content_type == ContentType.DOCUMENT:
                medias.append(
                    types.InputMediaDocument(
                        media=m.document.file_id,
                        caption=m.html_text
                    )
                )    
            elif m.content_type == ContentType.ANIMATION:
                medias.append(
                    types.InputMediaAnimation(
                        media=m.animation.file_id,
                        caption=m.html_text
                    )
                )    
            elif m.content_type == ContentType.AUDIO:
                medias.append(
                    types.InputMediaAudio(
                        media=m.audio.file_id,
                        caption=m.html_text
                    )
                )    
                
        await bot.send_media_group(
            chat_id=anon_user.id,
            media=medias,
        )
        
        await bot.send_message(
            chat_id=anon_user.id,
            text=_(MSG_NEW_QUESTION).format(msg=""),
            reply_markup=answer_button(current_user.id)
        )
    except Exception as e:
        await messages[-1].reply(_(MSG_SOMETHING_WENT_WRONG))
        logging.debug("Nimadir xato ketti" + str(e))
        return
    
    link = referal_link(current_user.id)
    await messages[-1].reply(
        text=_(MSG_SENT).format(link=link),
        reply_markup=share_button(link=link)
    )
    mention1 = "@" + current_user.username if current_user.username else current_user.mention_html()
    mention2 = "@" + anon_user.username if anon_user.username else anon_user.html_mention()
    await bot.send_message(
        chat_id=LOGS_CHANNEL,
        text=f"Anonym message was sent.\n"
            f"From {mention1} [<code>{current_user.id}</code>] "
            f"to {mention2} [<code>{anon_user.id}</code>]\n"
            f"Content_type: MediaGroup"
    )
    