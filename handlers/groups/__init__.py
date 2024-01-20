from aiogram import Router, F

from .start import router as start_router

group_router = Router(name="Group router")
group_router.message.filter(F.chat.type.in_(["group", "supergroup"]))

group_router.include_router(start_router)
