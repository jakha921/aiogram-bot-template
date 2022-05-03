from aiogram import types

from utils.misc.product import Product


pizza = Product(
    title="Bellisimo Pizza",
    description="Пепперони сердце",
    currency="UZS",
    prices=[
        types.LabeledPrice(
        label="Пицца",
        amount=5000000,       #50.000.00 UZS
    ),
        types.LabeledPrice(
        label="Доставка",
        amount=1200000      #12.000.00 UZS
    ),
    ],
    start_parameter="create_order",
    photo_url="https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F03650000-6bec-ac1f-7b66-08da0011769d.jpg&w=750&q=75",
    photo_width=800,
    photo_height=600,
    need_email=True,
    need_name=True,
    need_phone_number=True,    
)

book = Product(
    title='Война и мир',
    description='Алексондр Сергеевич Толстой',
    start_parameter='order_book',
    currency='UZS',
    prices=[
        types.LabeledPrice(
        label='Книга',
        amount=4000000,
        ),
        types.LabeledPrice(
            label='Доставка',
            amount=1200000,
        ),
    ],
    photo_url='https://pbs.twimg.com/media/EWxVndaXsAQGCzm.jpg',
    photo_width=900,
    photo_height=750,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True,
)


regular_shipping = types.ShippingOption(
    id='regular',
    title='Доставка за неделю',
    prices=[
        types.LabeledPrice(
            label='7 дней',
            amount=200000,
        )],
)

fast_shipping = types.ShippingOption(
    id='fast',
    title='Доставка за день',
    prices=[
        types.LabeledPrice(
        label='1 день',
        amount=300,
    )]
)

pickup_shipping = types.ShippingOption(
    id='pickup',
    title='Самовывоз',
    prices=[
        types.LabeledPrice(
            label='Скидка',
            amount=-1200000,
        )
    ]
)