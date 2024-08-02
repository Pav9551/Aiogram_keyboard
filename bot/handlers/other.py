from aiogram import Dispatcher, Bot
from aiogram.types import Message
from bot.keyboards import get_admin_keyboard,  get_feedback_keyboard
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from bot.misc import TgKeys
async def other_messages(msg: Message) -> None:
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Я вас не понял, напишите /start!")


async def __get_id(msg: Message) -> None:
    bot: Bot = msg.bot
    user = msg.from_user
    await bot.send_message(user.id, f"{user.username}: {user.id}")

async def __admin_exit(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы вышли из панели администратора ⚠️",
                           reply_markup=get_admin_keyboard(user_id))

async def __start(msg: Message) -> None:
    bot: Bot = msg.bot
    user = msg.from_user
    await bot.send_message(user.id, f"{user.username}: {'Это команда старт'}")
    await bot.send_message(user.id, 'Ваш ответ ...', reply_markup=get_feedback_keyboard(user.id))




async def __analytic(query: CallbackQuery) -> None:


    text = (
        'Отчет:\n',
        f'Кол-во пользователей: ',
        f'Кол-во сессий: \n',
        f'Total онлайн: ',
    )
    await query.answer('\n'.join(text), show_alert=True, cache_time=0)


def register_admin_handlers(dp: Dispatcher) -> None:
    # region Msg handlers


    # endregion

    # region Callback handlers

    dp.register_callback_query_handler(__analytic, True, lambda c: c.data == "analytics",
                                       state=True)

    # endregion

    #_get_auth_handlers(dp)


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__get_id, commands=["id"])
    dp.register_message_handler(__start, commands=["start"])
    dp.register_message_handler(other_messages, content_types=['text'], state=None)


id_for_answer = TgKeys.ID_FOR_ANSWER
async def __rate_clarity_full(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Ясность полная",
                           reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Ясность полная")

async def __rate_almost_perfect(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Почти идеально", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Почти идеально")

async def __rate_good_but_some_nuances(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Хорошо, но есть нюансы", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Хорошо, но есть нюансы")

async def __rate_clear_but_dry(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Понятно, но суховато", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Понятно, но суховато")

async def __rate_average(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Средненько", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Средненько")

async def __rate_somewhat_unclear(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Местами непонятно", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Местами непонятно")

async def __rate_difficult(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Сложновато", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Сложновато")

async def __rate_confusing(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Запутанно", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer, "Запутанно")

async def __rate_very_difficult(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Очень сложно", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer, "Очень сложно")

async def __rate_nonsense(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Ты втираешь мне какую-то дичь", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer, "Ты втираешь мне какую-то дичь")




def register_keyboards_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(__admin_exit, lambda c: c.data == "admin_exit")
    dp.register_callback_query_handler(__rate_clarity_full, lambda c: c.data == "rate_clarity_full")
    dp.register_callback_query_handler(__rate_almost_perfect, lambda c: c.data == "rate_almost_perfect")
    dp.register_callback_query_handler(__rate_good_but_some_nuances, lambda c: c.data == "rate_good_but_some_nuances")
    dp.register_callback_query_handler(__rate_clear_but_dry, lambda c: c.data == "rate_clear_but_dry")
    dp.register_callback_query_handler(__rate_average, lambda c: c.data == "rate_average")
    dp.register_callback_query_handler(__rate_somewhat_unclear, lambda c: c.data == "rate_somewhat_unclear")
    dp.register_callback_query_handler(__rate_difficult, lambda c: c.data == "rate_difficult")
    dp.register_callback_query_handler(__rate_confusing, lambda c: c.data == "rate_confusing")
    dp.register_callback_query_handler(__rate_very_difficult, lambda c: c.data == "rate_very_difficult")
    dp.register_callback_query_handler(__rate_nonsense, lambda c: c.data == "rate_nonsense")

