from aiogram import F, Router

from loader import i18n
from middlewares.i18n import MyI18nMiddleware
from middlewares.database import DatabaseMiddleware
from middlewares.throttling import ThrottlingMiddleware

from .help import router as help_router
from .about import router as about_router
from .start import router as start_router
from .cancel import router as cancel_router
from .unknown import router as unknown_router
from .language import router as language_router
from .questions import router as questions_router
from .anon_answer import router as answers_router
from .exceptions import router as exceptions_router


user_router = Router(name="User router")

user_router.message.filter(F.chat.type == 'private')

user_router.include_router(help_router)
user_router.include_router(start_router)
user_router.include_router(about_router)
user_router.include_router(cancel_router)
user_router.include_router(answers_router)
user_router.include_router(language_router)
user_router.include_router(questions_router)

user_router.include_router(unknown_router)
# user_router.include_router(exceptions_router)

user_router.message.middleware.register(DatabaseMiddleware())
user_router.message.middleware.register(ThrottlingMiddleware())
user_router.message.middleware.register(MyI18nMiddleware(i18n))

user_router.callback_query.middleware.register(DatabaseMiddleware())
user_router.callback_query.middleware.register(ThrottlingMiddleware())
user_router.callback_query.middleware.register(MyI18nMiddleware(i18n))


__all__ = ["router"]
