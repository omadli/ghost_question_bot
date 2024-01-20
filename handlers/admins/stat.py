from datetime import datetime, timedelta
from aiogram import types, Router
from aiogram.filters import Command

from db.models import DbUser
from settings import ADMINS


router = Router()

@router.message(Command("stat"))
async def cmd_stat(msg: types.Message):
    count_admins = len(ADMINS)
    count_users = await DbUser.all().count()
    count_active_users = await DbUser.filter(is_active=True).count()
    
    now = datetime.now()
    today = datetime(now.year, now.month, now.day)
    tomorrow = today + timedelta(days=1)
    count_today_joined = await DbUser.filter(join_date__range=(today, tomorrow)).count()
    
    last_week = today - timedelta(days=7)
    count_last_week_joined = await DbUser.filter(join_date__range=(last_week, tomorrow)).count()
    
    last_month = today - timedelta(days=30)
    count_last_month_joined = await DbUser.filter(join_date__range=(last_month, tomorrow)).count()
    
    
    await msg.answer(
        text=f"<b>📈Umumiy statistika📉</b>\n\n"
            f"Jami foydalanuvchilar: {count_users}\n"
            f"Aktiv foydalanuvchilar: {count_active_users}\n"
            f"⭐️Adminlar: {count_admins}\n"
            f"📅Bugun qo'shilganlar: {count_today_joined}\n"
            f"📆Oxirgi 1 haftada qo'shilganlar: {count_last_week_joined}\n"
            f"🗓Oxirgi 1 oyda qo'shilganlar: {count_last_month_joined}\n\n"
    )
