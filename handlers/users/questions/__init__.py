from aiogram import Router
from aiogram.filters import StateFilter

from .media_group import router as media_group_router
from .audio_message import router as audio_router
from .photo_message import router as photo_router
from .text_message import router as text_router
from .voice_message import router as voice_router
from .video_message import router as video_router


router = Router(name="Questions")
router.message.filter(StateFilter("anonchat"))

router.include_router(media_group_router)
router.include_router(text_router)
router.include_router(photo_router)
router.include_router(audio_router)
router.include_router(voice_router)
router.include_router(video_router)



__all__ = ["router"]
