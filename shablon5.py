from PIL import Image, ImageDraw, ImageFont


def shablon_6(texts):
    shablon, text_one, text_two, height_2, text_three, height_3, text_four, height_4 = texts

    text_one = str(text_one)
    text_two = [str(text_two), int(height_2)]
    text_three = [str(text_three), int(height_3)]
    text_four = [str(text_four), int(height_4)]

    text_two[1] = str((int(text_two[1])))
    text_three[1] = str((int(text_three[1])))
    text_four[1] = str((int(text_four[1])))

    im = Image.open('shablon5_ref.png')
    font = ImageFont.truetype('Intro Regular.ttf', size=80)
    font_2 = ImageFont.truetype('Intro Regular.ttf', size=40)
    font_3 = ImageFont.truetype('Intro Regular.ttf', size=50)
    #text_one = input()
    #text_two = input().split(",")
    #text_three = input().split(",")
    #text_four = input().split(",")
    draw_text = ImageDraw.Draw(im)
    draw = ImageDraw.Draw(im)
    draw_text.text((35, 30), text_one, font=font, fill=(102, 102, 102))

    draw_text.text((90, 258), text_two[0], font=font_2, fill=(102, 102, 102))
    draw.rectangle(((90, 308), (90 + (int(text_two[1]) * 6.84), 386)), fill=(102, 102, 102))

    draw_text.text((90, 448), text_three[0], font=font_2, fill=(102, 102, 102))
    draw.rectangle(((90, 498), (90 + (int(text_three[1]) * 6.84), 576)), fill=(102, 102, 102))

    draw_text.text((90, 637), text_four[0], font=font_2, fill=(102, 102, 102))
    draw.rectangle(((90, 687), (90 + (int(text_four[1]) * 6.84), 765)), fill=(102, 102, 102))

    im.save("image.png")

shablon_6([1, 2, 3, 100, 5, 6, 7, 8])