from typing import Final
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


KB_CANCEL_SETUP: Final = InlineKeyboardMarkup(1)
KB_CANCEL_SETUP.add(
    InlineKeyboardButton("Отменить", callback_data="cancel_setup")
)

KB_INFO: Final = InlineKeyboardMarkup(1)
KB_INFO.add(
    InlineKeyboardButton("LET'S GO!", url='https://telegra.ph/Kommandy-bota-09-14')
)
