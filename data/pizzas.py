from aiogram import types
from keyboards.inline.photoInline import photo_key


pizzas = [
    {
        'id' : '001',
        'title' : 'Пепперони сердце',
        'description': 'Удивите свою вторую половинку необычной пиццей ❤️ Колбаски пепперони, нежный сыр моцарелла и томатный соус 😋',
        'cost' : '79 000',
        'url': 'https://bellissimo.uz/ru#Pizza',
        'thumb_url' : 'https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F6d45a283-a19c-4cea-a45a-99a4b690e0cf.jpg&w=750&q=75',
        
    },
    {
        'id' : '002',
        'title' : 'Сальса',
        'description': 'Цыпленок, соус сальса, нежный сыр моцарелла, халапеньо, болгарский перец и томаты',
        'cost' : '50 000',
        'url': 'https://bellissimo.uz/ru#Pizza',
        'thumb_url' : 'https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F2c814f26-9d3c-4b66-ae54-003fe4db2cb4.jpg&w=750&q=75',
    },
    {
        'id' : '003',
        'title' : 'Гурме',
        'description': 'Пицца соус, маслины, пепперони, грибы, орегано',
        'cost' : '50 000',
        'url': 'https://bellissimo.uz/ru#Pizza',
        'thumb_url' : 'https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F2c814f26-9d3c-4b66-ae54-003fe4db2cb4.jpg&w=750&q=75',
    },
    {
        'id' : '004',
        'title' : 'Супер Микс',
        'description': 'Пицца «Супер Микс» Сочетание 4х любимых вкусов в 1 пицце 😋 Отлично подойдёт для тех кто любит всё и сразу 🙃',
        'cost' : '80 000',
        'url': 'https://bellissimo.uz/ru#Pizza',
        'thumb_url' : 'https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F94844930-5c66-4c12-a670-93b048169dbe.jpg&w=750&q=75',
    },
    {
        'id' : '005',
        'title' : 'Чиккен карри',
        'description': 'Говяжий рулет и куриное филе в сочетании с сыром моцарелла, ананасами и соусом карри',
        'cost' : '50 000',
        'url': 'https://bellissimo.uz/ru#Pizza',
        'thumb_url' : 'https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F45bd4064-2430-4250-899d-d6f834d36c30.jpg&w=750&q=75',
    },
]

inline_result_pizza = []
for pizza in pizzas:
    inline_result_pizza.append(
        types.InlineQueryResultArticle(
            id=pizza['id'],
            title=pizza['title'],
            input_message_content=types.InputTextMessageContent(
                message_text=f'{pizza["thumb_url"]}\n{pizza["description"]}\nЦена: <b>{pizza["cost"]} сум</b>', 
                parse_mode='HTML',
            ),
            thumb_url=pizza['thumb_url'],
            description=f'{pizza["description"][:30]}...\nЦена: {pizza["cost"]} сум',
            url=pizza['url'],
            hide_url=True,
            reply_markup=photo_key,
            
        )
    )


