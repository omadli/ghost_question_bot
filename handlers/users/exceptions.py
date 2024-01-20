import logging
from aiogram import Router
from aiogram import types


router = Router()

@router.error()
async def handle_errors(event: types.ErrorEvent):
    logging.debug(event)
    logging.debug(event)
    return True
