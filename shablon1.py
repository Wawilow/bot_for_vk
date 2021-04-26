from PIL import Image, ImageDraw, ImageFont

def shablon_1(texts):
    shablon, text_one, text_two, text_three, text_four = texts
    im = Image.open('shablon1_ref.png')
    font = ImageFont.truetype('Intro Regular.ttf', size=80)
    font_2 = ImageFont.truetype('Intro Regular.ttf', size=40)
    draw_text = ImageDraw.Draw(im)
    draw_text.text((35, 30), text_one, font=font, fill=(102, 102, 102))
    draw_text.text((665, 465), text_two, font=font_2, fill=(102, 102, 102))
    draw_text.text((665, 550), text_three, font=font_2, fill=(102, 102, 102))
    draw_text.text((665, 635), text_four, font=font_2, fill=(102, 102, 102))
    '''im.show()'''
    im.save("image.png")