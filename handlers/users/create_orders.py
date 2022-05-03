from aiogram import types

from loader import dp, bot
from data.products import pizza, book, regular_shipping, fast_shipping, pickup_shipping
from keyboards.inline.create_keyboard import build_keyboard



@dp.message_handler(commands='order_pizza')
async def orger_pizza(msg: types.Message):
    caption = 'Удивите свою <b>вторую половинку</b> необычной пиццей ❤️ '
    caption += 'Колбаски пепперони, нежный сыр моцарелла и томатный соус 😋'
    caption += '\n\nСтоимость: <b>50.000.00</b> UZS'
    photo_url = 'https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F6d45a283-a19c-4cea-a45a-99a4b690e0cf.jpg&w=750&q=75'
    await msg.answer_photo(photo_url, caption=caption, parse_mode='HTML', reply_markup=build_keyboard('pizza'))


@dp.message_handler(commands='order_book')
async def order_book(msg: types.Message):
    caption = 'Война и мир. Алексондр Сергеевич Толстой\n'
    caption += 'Роман-эпопея <i>Льва Николаевича Толстого</i>, описывающий русское общество в эпоху войн против Наполеона в 1805-1812 годах. \n'
    caption += 'Эпилог романа доводит повествование до 1820 года.'
    caption += '\n\nСтоимость: <b>4 USD</b>'
    photo_url = 'https://pbs.twimg.com/media/EWxVndaXsAQGCzm.jpg'
    await msg.answer_photo(photo_url, caption=caption, parse_mode='HTML', reply_markup=build_keyboard('book'))
    

# create invoice
@dp.callback_query_handler(text="product:book")
async def book_invoice(call: types.CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id, 
                           **book.generate_invoice(),
                            payload="123456")
    await call.answer()
    
@dp.callback_query_handler(text="product:pizza")
async def book_invoice(call: types.CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                          **pizza.generate_invoice (),
                            payload="123457")
    await call.answer()


# check addres
@dp.shipping_query_handler ()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Мы не можем доставить за гранизу")
        
    elif query.shipping_address.city.lower() == "tashkent":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[regular_shipping, fast_shipping, pickup_shipping],
                                        ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[regular_shipping],
                                        ok=True)