from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
import buttons

# Finite State Machine - FSM

class FSM_reg(StatesGroup):
    fullname = State()
    date = State()
    email = State()
    phone = State()
    address = State()
    gender = State()
    country = State()
    photo = State()
    submit = State()


async def start_fsm_reg(message: types.Message):
    await message.answer('Введите фио: ', reply_markup=buttons.cancel_button)
    await FSM_reg.fullname.set()


async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await message.answer('Введите дату рождения:')
    await FSM_reg.next()


async def load_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer('Введите email:')
    await FSM_reg.next()


async def load_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await message.answer('Введите номер телефона:')
    await FSM_reg.next()


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer('Введите адрес:')
    await FSM_reg.next()


async def load_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await message.answer('Введите свой пол:')
    await FSM_reg.next()


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await message.answer('В какой стране проживаете:')
    await FSM_reg.next()


async def load_country(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['country'] = message.text
    await message.answer('Отправьте фото:')
    await FSM_reg.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data['photo'],
                               caption=f'Верные ли данные?\n\n'
                                       f'ФИО: {data["fullname"]}\n'
                                       f'Дата рождения: {data["date"]}\n'
                                       f'Эл.Почта: {data["email"]}\n'
                                       f'Номер телефона: {data["phone"]}\n'
                                       f'Адрес: {data["address"]}\n'
                                       f'Пол: {data["gender"]}\n'
                                       f'Страна: {data["country"]}\n',
                               reply_markup=buttons.submit_button)
    await FSM_reg.next()


async def submit(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()

    if message.text == 'Да':
        await message.answer('Отлично, Данные в базе!', reply_markup=kb)
        await state.finish()

    elif message.text == 'Нет':
        await message.answer('Хорошо, заполнение анкеты завершено!', reply_markup=kb)
        await state.finish()

    else:
        await message.answer('Выберите "Да" или "Нет"')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    kb = ReplyKeyboardRemove()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=kb)


def register_fsm_reg(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена', ignore_case=True), state="*")

    dp.register_message_handler(start_fsm_reg, commands=['reg'])
    dp.register_message_handler(load_fullname, state=FSM_reg.fullname)
    dp.register_message_handler(load_date, state=FSM_reg.date)
    dp.register_message_handler(load_email, state=FSM_reg.email)
    dp.register_message_handler(load_phone, state=FSM_reg.phone)
    dp.register_message_handler(load_address, state=FSM_reg.address)
    dp.register_message_handler(load_gender, state=FSM_reg.gender)
    dp.register_message_handler(load_country, state=FSM_reg.country)
    dp.register_message_handler(load_photo, state=FSM_reg.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_reg.submit)