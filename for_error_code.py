from PIL import Image, ImageDraw, ImageFont
import random


def debil_image():
    im = Image.new('RGB', (500, 500), color=(0, 0, 0))
    font_0 = ImageFont.truetype('Intro Regular.ttf', size=60)
    font = ImageFont.truetype('Intro Regular.ttf', size=50)
    font_2 = ImageFont.truetype('Intro Regular.ttf', size=40)
    draw_text = ImageDraw.Draw(im)
    fraces = ['вводи нормально', 'неправильный ввод', 'попробуй еще раз', 'делай внимательнее', 'попробуй еще',
              'ты глупый?', 'code_', 'code__', 'code1_', 'code_1', 'code2_', 'code_2', 'code3_', 'code_3', 'code4_',
              'code_4', 'code5_', 'code_5']
    text = random.choice(fraces)
    if 17 <= len(text) >= 15:
        draw_text.text((10, 225), text, font=font, fill=(255, 0, 0))
    elif len(text) < 15:
        if text == 'code_':
            text_1 = 'внимательно читай'
            text_2 = 'требования бота'
            draw_text.text((10, 195), text_1, font=font, fill=(255, 0, 0))
            draw_text.text((10, 255), text_2, font=font, fill=(255, 0, 0))

        elif text == 'code__':
            text_1 = 'твой ввод'
            text_2 = 'некорректен'
            draw_text.text((10, 195), text_1, font=font, fill=(255, 0, 0))
            draw_text.text((10, 255), text_2, font=font, fill=(255, 0, 0))

        elif text == 'code1_':
            text_1 = 'не то вводишь,'
            text_2 = 'читай условия'
            draw_text.text((10, 195), text_1, font=font, fill=(255, 0, 0))
            draw_text.text((10, 255), text_2, font=font, fill=(255, 0, 0))

        elif text == 'code_1':
            text_1 = 'еще раз прочитай'
            text_2 = 'требования бота,'
            text_3 = 'пожалуйста'
            draw_text.text((10, 180), text_1, font=font, fill=(255, 0, 0))
            draw_text.text((10, 245), text_2, font=font, fill=(255, 0, 0))
            draw_text.text((10, 310), text_3, font=font, fill=(255, 0, 0))

        elif text == 'code2_':
            text_1 = 'еще раз просмотри'
            text_2 = 'требования бота,'
            text_3 = 'пожалуйста'
            draw_text.text((10, 180), text_1, font=font, fill=(255, 0, 0))
            draw_text.text((10, 245), text_2, font=font, fill=(255, 0, 0))
            draw_text.text((10, 310), text_3, font=font, fill=(255, 0, 0))

        elif text == 'code_2':
            text_1 = 'еще раз просмотри'
            text_2 = 'сообщение бота,'
            text_3 = 'пожалуйста'
            draw_text.text((10, 180), text_1, font=font, fill=(255, 0, 0))
            draw_text.text((10, 245), text_2, font=font, fill=(255, 0, 0))
            draw_text.text((10, 310), text_3, font=font, fill=(255, 0, 0))

        elif text == 'code3_':
            text_1 = 'неправильный'
            text_2 = 'ввод'
            text_3 = 'информации'
            draw_text.text((10, 180), text_1, font=font, fill=(255, 0, 0))
            draw_text.text((10, 245), text_2, font=font, fill=(255, 0, 0))
            draw_text.text((10, 310), text_3, font=font, fill=(255, 0, 0))

        elif text == 'code_3':
            text_1 = 'введенная вами'
            text_2 = 'информация'
            text_3 = 'некорректна'
            draw_text.text((10, 180), text_1, font=font, fill=(255, 0, 0))
            draw_text.text((10, 245), text_2, font=font, fill=(255, 0, 0))
            draw_text.text((10, 310), text_3, font=font, fill=(255, 0, 0))

        elif text == 'code4_':
            text_1 = 'попробуйте еще раз:'
            text_2 = 'неправильный,'
            text_3 = 'ввод'
            draw_text.text((10, 180), text_1, font=font_2, fill=(255, 0, 0))
            draw_text.text((10, 245), text_2, font=font, fill=(255, 0, 0))
            draw_text.text((10, 310), text_3, font=font, fill=(255, 0, 0))

        elif text == 'code_4':
            text_1 = 'ошибка:'
            text_2 = 'неправильный'
            text_3 = 'ввод информации'
            text_4 = 'пользователем'
            draw_text.text((10, 160), text_1, font=font_2, fill=(255, 0, 0))
            draw_text.text((10, 225), text_2, font=font, fill=(255, 0, 0))
            draw_text.text((10, 290), text_3, font=font, fill=(255, 0, 0))
            draw_text.text((10, 355), text_3, font=font, fill=(255, 0, 0))

        elif text == 'code5_':
            text_1 = 'пожалуйста'
            text_2 = 'внимательнее'
            text_3 = 'читайте требования'
            text_4 = 'бота'
            draw_text.text((10, 160), text_1, font=font_2, fill=(255, 0, 0))
            draw_text.text((10, 225), text_2, font=font, fill=(255, 0, 0))
            draw_text.text((10, 290), text_3, font=font, fill=(255, 0, 0))
            draw_text.text((10, 355), text_3, font=font, fill=(255, 0, 0))

        elif text == 'code_6':
            text_1 = 'пожалуйста'
            text_2 = 'внимательнее'
            text_3 = 'выполняйте просьбы'
            text_4 = 'бота'
            draw_text.text((10, 160), text_1, font=font_2, fill=(255, 0, 0))
            draw_text.text((10, 225), text_2, font=font, fill=(255, 0, 0))
            draw_text.text((10, 290), text_3, font=font, fill=(255, 0, 0))
            draw_text.text((10, 355), text_3, font=font, fill=(255, 0, 0))

        else:
            draw_text.text((10, 225), text, font=font_0, fill=(255, 0, 0))
    else:
        draw_text.text((10, 225), text, font=font_2, fill=(255, 0, 0))

    im.save("image.png")