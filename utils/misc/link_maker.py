from loader import bot
from .id_cipher import cipher


def referal_link(user_id: int):
    return "https://t.me/" + bot._me.username + "?start=" + cipher(user_id)
