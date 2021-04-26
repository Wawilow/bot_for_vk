from PIL import Image, ImageDraw, ImageFont
import sys
import locale


def shablon_6(texts):
    # texts = input().split()
    # texts = "Круги_Эйлера 123456789 123456789 123456789 123456789 123456789 123456789 123456789".split()
    text_eight = ''
    kaf, shablon, text_one, text_two, text_three, text_four, text_five, text_six, text_seven = texts

    font = ImageFont.truetype('Intro Regular.ttf', size=80)
    font_2 = ImageFont.truetype('Intro Regular.ttf', size=30)

    im = Image.open('shablon6_ref.jpg')
    draw_text = ImageDraw.Draw(im)
    draw = ImageDraw.Draw(im)

    x = 25
    y = 50

    draw_text.text((35, 30), shablon, font=font, fill=(102, 102, 102))
    draw_text.text((140 + x, 380 + y), text_one, font=font_2, fill=(102, 102, 102))
    draw_text.text((595 + x, 365 + y), text_two, font=font_2, fill=(102, 102, 102))
    draw_text.text((300 + x, 740 + y), text_three, font=font_2, fill=(102, 102, 102))
    draw_text.text((260 + x, 600 + y), text_four, font=font_2, fill=(102, 102, 102))
    draw_text.text((400 + x, 320 + y), text_five, font=font_2, fill=(102, 102, 102))
    draw_text.text((520 + x, 610 + y), text_six, font=font_2, fill=(102, 102, 102))
    draw_text.text((390 + x, 500 + y), text_seven, font=font_2, fill=(102, 102, 102))

    im.save("image.png")