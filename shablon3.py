from PIL import Image, ImageDraw, ImageFont


def shablon_3(texts):
    shablon, text_one, text_two, height_2, text_three, height_3, text_four, height_4 = texts
    im = Image.open('shablon3_ref.png')
    font = ImageFont.truetype('Intro Regular.ttf', size=80)
    font_2 = ImageFont.truetype('Intro Regular.ttf', size=40)
    font_3 = ImageFont.truetype('Intro Regular.ttf', size=50)
    text_one = text_one
    text_two = [text_two, height_2]
    text_three = [text_three, height_3]
    text_four = [text_four, height_4]

    text_two[1] = str((int(text_two[1])))
    text_three[1] = str((int(text_three[1])))
    text_four[1] = str((int(text_four[1])))

    text_two.append(str((int(text_two[1]) // 3) * 2))
    text_three.append(str((int(text_three[1]) // 3) * 2))
    text_four.append(str((int(text_four[1]) // 3) * 2))
    #text_one = input()
    #text_two = input().split(",")
    #text_three = input().split(",")
    #text_four = input().split(",")
    draw_text = ImageDraw.Draw(im)
    draw = ImageDraw.Draw(im)
    draw_text.text((35, 30), text_one, font=font, fill=(102, 102, 102))

    draw_text.text((170, 850), text_two[0], font=font_2, fill=(102, 102, 102))
    draw.rectangle(((210, 830 - (int(text_two[2]) * 8)), (250, 830)), fill=(50, 50, 50))
    draw_text.text((190, 830 - (int(text_two[2]) * 8) - 50), str(int(text_two[1])) + "%", font=font_3, fill=(50, 50, 50))

    draw_text.text((440, 850), text_three[0], font=font_2, fill=(102, 102, 102))
    draw.rectangle(((480, 830 - (int(text_three[2]) * 8)), (520, 830)), fill=(50, 50, 50))
    draw_text.text((460, 830 - (int(text_three[2]) * 8) - 50), str(int(text_three[1])) + "%", font=font_3, fill=(50, 50, 50))

    draw_text.text((710, 850), text_four[0], font=font_2, fill=(102, 102, 102))
    draw.rectangle(((750, 830 - (int(text_four[2]) * 8)), (790, 830)), fill=(50, 50, 50))
    draw_text.text((730, 830 - (int(text_four[2]) * 8) - 50), str(int(text_four[1])) + "%", font=font_3, fill=(50, 50, 50))

    '''im.show()'''
    im.save("image.png")


hu_make = {'user_id': [False, False, False, False, False, False, False, False]}
print(hu_make)