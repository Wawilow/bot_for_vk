import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randrange
import shablon1
import shablon3
import shablon6
import shablon5
import for_error_code
import sql_work


hu_make = {}
token = 'f626cee422e9d40baf72cdb457b391a82fe1ba7a8cb5968be52f4094504a2ddedc4df00cf098ad5bdb454'#токен от левой группы
# не надейся
vk = vk_api.VkApi(token=token)
api = vk.get_api()
longpoll = VkLongPoll(vk)
# это сообщение выводится в help
all_shab_text = 'Что бы выбрать шаблон напишите номер шаблона, в сообщении должна быть только цифра' \
                '\n Шаблон 1 - круговая диограмма. "1"' \
                '\n Шаблон 3 - столбы вертикальные. "3"' \
                '\n Шаблон 5 - столбы горизонтальные "5"'\
                '\n Шаблон 6 - круги эллера "6"'
#вс для help
all_comands = 'Все команды бота ' \
              '\n Начать(go) - начинает создание мема, дальше следуем инструкции' \
              '\n Стоп(stop) - останавливает создание мема, если где то ошиблись то придется все заново вводить' \
              '\n Помоги(help) - команда выводит вот это сообщение'

class Test_Bot:
    def __init__(self, user_id):
        print("\nСоздан объект бота!")

        self._USER_ID = user_id
        begin = ['GO', 'НАЧАТЬ', 'ПОГНАЛИ', 'ПОЕХАЛИ', 'СТАРТ']
        help = ['HELP', 'ПОМОГИ', 'ПОМОЩ', 'ЧЕГО БЛЯТЬ', 'КОМАНДЫ']
        stop = ['STOP', 'СТОП', 'АСТАНОВИСЬ']
        good_bye = ['GOOD BAY', 'ПОКА']
        self._COMMANDS = [begin, help, stop, good_bye]

    def new_message(self, message, user_id):
        if message.upper() in self._COMMANDS[2]:
            if user_id in hu_make:
                del hu_make[user_id]
                return 'Создание мема отмененно'
            else:
                return 'Вы не делали мем пока что'
        elif len(hu_make) != 0:
            if user_id in hu_make:
                if not hu_make[user_id][0]:
                    hu_make[user_id][0] = message
                    present_shablon(user_id)
                    return f'Начинаем формирование мема, введи текст заголовка' \
                           f'\n Что бы остановить создание напищи Stop'
                if hu_make[user_id][0] == '1':
                    if not hu_make[user_id][1]: #заголовок
                        hu_make[user_id][1] = message
                        return 'Заголовок определен, введи название доли номер 1'
                    if not hu_make[user_id][2]:  # пункт 1
                        hu_make[user_id][2] = message
                        return 'Название первой доли определено, введи название доли номер 2'
                    if not hu_make[user_id][3]:  # пункт 2
                        hu_make[user_id][3] = message
                        return 'Название второй доли определено, введи название доли номер 3'
                    if not hu_make[user_id][4]:  # пункт 3
                        hu_make[user_id][4] = message
                        how_shalon(user_id)
                        return 'Готово'
                elif hu_make[user_id][0] == '3':
                    if not hu_make[user_id][1]:
                        for _ in range(3):#заголовок
                            hu_make[user_id].append(False)
                        hu_make[user_id][1] = message
                        return 'Заголовок  определен, введи название первого столба'
                    if not hu_make[user_id][2]:  # пункт 1
                        hu_make[user_id][2] = message
                        return 'Название первого столба определено, введи высоту столба от 1 до 100'
                    if not hu_make[user_id][3]:  # пункт 1
                        if is_number_like(message):
                            hu_make[user_id][3] = message
                            return 'Высота первого столба определена, введи название второго столба'
                        else:
                            return 'То что вы ввели либо не число, либо оно не в промежутке от 1 до 100'
                    if not hu_make[user_id][4]:  # пункт 2
                        hu_make[user_id][4] = message
                        return 'Название второго столба определено, введи высоту столба от 1 до 100'
                    if not hu_make[user_id][5]:  # пункт 2
                        if not hu_make[user_id][5]:  # пункт 1
                            if is_number_like(message):
                                hu_make[user_id][5] = message
                                return 'Высота первого столба определено, введи название третьего столба'
                            else:
                                return 'То что вы ввели либо не число, либо оно не в промежутке от 1 до 100'
                    if not hu_make[user_id][6]:  # пункт 3
                        hu_make[user_id][6] = message
                        return 'Название третьего столба определено, введи высоту столба от 1 до 100'
                    if not hu_make[user_id][7]:  # пункт 3
                        if not hu_make[user_id][7]:  # пункт 1
                            if is_number_like(message):
                                hu_make[user_id][7] = message
                                how_shalon(user_id)
                                return 'Готово'
                            else:
                                return 'То что вы ввели либо не число, либо оно не в промежутке от 1 до 100'
                elif hu_make[user_id][0] == '5':
                    if not hu_make[user_id][1]:
                        for _ in range(3):#заголовок
                            hu_make[user_id].append(False)
                        hu_make[user_id][1] = message
                        return 'Заголовок  определен, введи название первого столба'
                    if not hu_make[user_id][2]:  # пункт 1
                        hu_make[user_id][2] = message
                        return 'Название первого столба определено, введи длину столба от 1 до 100'
                    if not hu_make[user_id][3]:  # пункт 1
                        if is_number_like(message):
                            hu_make[user_id][3] = message
                            return 'Длина первого столба определена, введи название второго столба'
                        else:
                            return 'То что вы ввели либо не число, либо оно не в промежутке от 1 до 100'
                    if not hu_make[user_id][4]:  # пункт 2
                        hu_make[user_id][4] = message
                        return 'Название второго столба определено, введи длину столба от 1 до 100'
                    if not hu_make[user_id][5]:  # пункт 2
                        if not hu_make[user_id][5]:  # пункт 1
                            if is_number_like(message):
                                hu_make[user_id][5] = message
                                return 'Длина первого столба определено, введи название третьего столба'
                            else:
                                return 'То что вы ввели либо не число, либо оно не в промежутке от 1 до 100'
                    if not hu_make[user_id][6]:  # пункт 3
                        hu_make[user_id][6] = message
                        return 'Название третьего столба определено, введи длину столба от 1 до 100'
                    if not hu_make[user_id][7]:  # пункт 3
                        if not hu_make[user_id][7]:  # пункт 1
                            if is_number_like(message):
                                hu_make[user_id][7] = message
                                how_shalon(user_id)
                                return 'Готово'
                            else:
                                return 'То что вы ввели либо не число, либо оно не в промежутке от 1 до 100'
                elif hu_make[user_id][0] == '6':
                    if not hu_make[user_id][1]:
                        for _ in range(4):#заголовок
                            hu_make[user_id].append(False)
                        hu_make[user_id][1] = message
                        return 'Заголовок  определен, введи название доли 1'
                    if not hu_make[user_id][2]:  # пункт 1
                        hu_make[user_id][2] = message
                        return 'Название доли 1 определено, введи название доли 2'
                    if not hu_make[user_id][3]:  # пункт 1
                        hu_make[user_id][3] = message
                        return 'Название доли 2 определено, введи название доли 3'
                    if not hu_make[user_id][4]:  # пункт 2
                        hu_make[user_id][4] = message
                        return 'Название доли 3 определено, введи название доли 13'
                    if not hu_make[user_id][5]:  # пункт 2
                        hu_make[user_id][5] = message
                        return 'Название доли 13 определено, введи название доли 12'
                    if not hu_make[user_id][6]:  # пункт 3
                        hu_make[user_id][6] = message
                        return 'Название доли 12 определено, введи название доли 23'
                    if not hu_make[user_id][7]:  # пункт 3
                        hu_make[user_id][7] = message
                        return 'Название доли 23 определено, введи название доли 123'
                    if not hu_make[user_id][8]:  # пункт 3
                        if not hu_make[user_id][8]:  # пункт 1
                            hu_make[user_id][8] = message
                            how_shalon(user_id)
                            return 'Готово'
                else:
                    how_shalon(user_id)
                    return 'Готово'

        coma_help = [f'{i[0]}' for i in self._COMMANDS]
        #print(message.upper() == self._COMMANDS[1].upper(), message == self._COMMANDS[1], message.lower())
        if message.upper() in self._COMMANDS[0]:#начать
            hu_make[user_id] = [False, False, False, False, False]
            return f'Выберити шаблон \n {all_shab_text}'
        elif message.upper() in self._COMMANDS[1]:#help
            return f'\n{all_comands}'
        elif message.upper() in self._COMMANDS[2]:#stop
            del hu_make[user_id]
            return f'Все шаблоны очищены'
        elif message.upper() in self._COMMANDS[3]:#stop
            return f'абоба'
        else:
            # print(message, self._COMMANDS[1], message.lower() == self._COMMANDS[1])
            return f'У меня нету этой команды, если ты хочешь узнать список команд напиши «help»'


def write_msg(user_id, message, phhoto):
    if message == 'Готово':
        write_msg_with_photo(user_id, message, phhoto)
    else:
        api.messages.send(user_id=user_id, message=str(message), random_id=randrange(999999999))


def write_msg_with_photo(user_id, message, phhoto):
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(str(phhoto))
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    api.messages.send(user_id=user_id, message=str(message), random_id=randrange(999999999),
                      attachment=attachment)


def how_shalon(user_id):
    sql_work.sql2(str(hu_make[user_id][1]), str(hu_make[user_id]))
    sql_work.sql3(user_id, hu_make[user_id][0], hu_make[user_id][1], hu_make[user_id][2:])
    if hu_make[user_id][0] == '1':
        shablon1.shablon_1(hu_make[user_id])
    elif hu_make[user_id][0] == '3':
        shablon3.shablon_3(hu_make[user_id])
    elif hu_make[user_id][0] == '5':
        shablon5.shablon_6(hu_make[user_id])
    elif hu_make[user_id][0] == '6':
        shablon6.shablon_6(hu_make[user_id])
    else:
        for_error_code.debil_image()
        print('проебался')
    del hu_make[user_id]

def present_shablon(user_id):
    shabl1 = 'shablon1_pres.jpg.png'
    shabl3 = 'shablon3_pres.jpg.png'
    shabl6 = 'shablon6_pres.jpg.png'
    print(hu_make[user_id])
    if hu_make[user_id][0] == '1':
        write_msg_with_photo(user_id, '', shabl1)
    elif hu_make[user_id][0] == '3':
        write_msg_with_photo(user_id, '', shabl3)
    elif hu_make[user_id][0] == '6':
        write_msg_with_photo(user_id, '', shabl6)
    else:
        print('проебался')


def is_number_like(x):
    try:
        int(x) + 1
    except:
        return False
    if 0 <= int(x) <= 100:
        return True
    else:
        return False


print("Server started")

while True:
#    if True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    sql_work.sql(event.user_id)
                    print()
                    print('New message:')
                    print(f'For me by: {event.user_id}', end='')
                    print(hu_make)


                    bot = Test_Bot(event.user_id)
                    write_msg(event.user_id, bot.new_message(event.text, event.user_id), 'image.png')
    except:
        print('Не паникуем')
