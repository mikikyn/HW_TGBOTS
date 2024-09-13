from config import bot, dp
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import sizes

class FSM_Store(StatesGroup):
    name=State()
    size=State()
    category=State()
    price=State()
    photo=State()

size=['XL', 'L', 'M']
async def fsm_start(message:types.Message):
    await message.answer('Название продукта?')
    await FSM_Store.name.set()

async def load_name(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await message.answer('Размер продукта?', reply_markup=sizes)
        await FSM_Store.size.set()

async def load_size(message:types.Message, state:FSMContext):
    if message.text in size:
        async with state.proxy() as data:
            data['size'] = message.text
        await message.answer('Категория продукта?', reply_markup=types.ReplyKeyboardRemove())
        await FSM_Store.next()
    else:
        await message.answer('Нажми на Кнопку!')

async def load_category(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer('Цена продукта?')
    await FSM_Store.next()

async def load_price(message:types.Message, state:FSMContext):
    if message.text.isdigit():

        async with state.proxy() as data:
            data['price'] = message.text
        await message.answer('Фото продукта?')
        await FSM_Store.next()
    else:
        await message.answer('Только цифры!')

async def load_photo(message:types.Message, state:FSMContext):
    photo=message.photo[-1].file_id
    async with state.proxy() as data:
        data['photo'] = photo
    await message.answer_photo(photo=photo,
                               caption='name: {data["name"]}\n'
                               f'size: {data["size"]}\n'
                               f'category: {data["category"]}\n'
                               f'price: {data["price"]}\n')

    await state.finish()
def register_fsm_store(dispatcher: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['product'])
    dp.register_message_handler(load_name, state=FSM_Store.name)
    dp.register_message_handler(load_size, state=FSM_Store.size)
    dp.register_message_handler(load_category, state=FSM_Store.category)
    dp.register_message_handler(load_price, state=FSM_Store.price)
    dp.register_message_handler(load_photo, state=FSM_Store.photo, content_types=['photo'])