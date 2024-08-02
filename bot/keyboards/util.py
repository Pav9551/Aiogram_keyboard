from copy import deepcopy

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
def get_admin_keyboard(user_id: int) -> InlineKeyboardMarkup:
    #user = get_user_by_telegram_id(user_id)
    #if not user.admin:
        #raise Exception()
    kb = InlineKeyboardMarkup(1)
    kb.add(
        InlineKeyboardButton("Добавить администратора ➕", callback_data="add_admin"),
        InlineKeyboardButton("Аналитика 🤌", callback_data="analytics"),
        InlineKeyboardButton("Рассылка ✉️", callback_data="advertising"),
        InlineKeyboardButton("Выйти ⛔️", callback_data="admin_exit"),
    )
    return kb
def get_feedback_keyboard(user_id: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(1)
    kb.add(
        InlineKeyboardButton("Ясность полная ➕", callback_data="rate_clarity_full"),
        InlineKeyboardButton("Почти идеально", callback_data="rate_almost_perfect"),
        InlineKeyboardButton("Хорошо, но есть нюансы", callback_data="rate_good_but_some_nuances"),
        InlineKeyboardButton("Понятно, но суховато", callback_data="rate_clear_but_dry"),
        InlineKeyboardButton("Средненько", callback_data="rate_average"),
        InlineKeyboardButton("Местами непонятно", callback_data="rate_somewhat_unclear"),
        InlineKeyboardButton("Сложновато", callback_data="rate_difficult"),
        InlineKeyboardButton("Запутанно", callback_data="rate_confusing"),
        InlineKeyboardButton("Очень сложно", callback_data="rate_very_difficult"),
        InlineKeyboardButton("Ты втираешь мне какую-то дичь ⛔️", callback_data="rate_nonsense"),
    )
    return kb


