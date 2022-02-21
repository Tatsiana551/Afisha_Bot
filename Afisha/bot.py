import telebot
from telebot import types
import const

bot = telebot.TeleBot(const.API_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_registration = types.KeyboardButton("Зарегистрировать событие")
    btn_Event_View = types.KeyboardButton("Посмотреть событие города")


    markup.add(btn_registration,btn_Event_View)

    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Зарегистрировать событие":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_town = types.KeyboardButton("Город")
            btn_type = types.KeyboardButton("Тип")
            btn_title = types.KeyboardButton("Название")
            btn_description = types.KeyboardButton("Описание")
            btn_place = types.KeyboardButton("Место")
            btn_date_and_time = types.KeyboardButton("Дата и время начало")
            btn_price = types.KeyboardButton("Стоимость входа")
            btn_link = types.KeyboardButton("Ссылка или телефон организатора")
            back = types.KeyboardButton("Назад")
            markup.add(btn_town, btn_type, btn_title, btn_description, btn_place, btn_date_and_time, btn_price, btn_link, back)

            bot.send_message(message.chat.id, "Зарегистрировать событие", reply_markup=markup)
        elif message.text == "Город":
            bot.send_message(message.chat.id,
                             "Список городов:\n"
                             "Заславль, Боровляны, Сеница, Юбилейный, Прилуки, Михановичи, Мачулищи,\n"
                             "Гатово, Ждановичи, Колодищи, Березино, Борисов, Жодино, Копыль, Логойск,\n"
                             "Любань, Марьина Горка, Мядель, Фаниполь, Джержинск, Несвиж, Слуцк,\n"
                             "Смолевичи, Червень, Осиповичи, Быхов, Горки, Климовичи, Кричев,\n"
                             "Черников, Гродно, Волковыск, Новогрудок, Речица, Рогочев, Поставы.\n")

        elif message.text == "Тип":
            bot.send_message(message.chat.id,
                             "Типы развлечений:\n"
                             "Медународные выставки, \n"
                             "Республиканские выставки,\n"
                             "Региональные выставки\n")


        elif message.text == "Название":
            bot.send_message(message.chat.id,
                             "Медународные выставки:\n"
                             "Международная специализированная выставка-ярмарка «Охота и рыболовство – 2022»: www.belexpo.by \n"
                             "Международная архитектурно-строительная выставка «BUDEXPO-2022»: www.budexpo.by \n"
                             "Международная выставка туристических услуг «ОТДЫХ-2022»: www.tourexpo.by\n "
                             "Международная специализированная выставка-ярмарка товаров и услуг для женщин «LADY EXPO»: www.ladyexpo.by\n"
                             "3-я международная специализированная выставка «МИР ЗОО»: mirzoo.by\n"
                             "Республиканские выставки:\n"
                             "Республиканская выставка авторских изделий “Чароўны Млын”:expolist@gmail.com \n"
                             "XII Республиканская выставка-интерактив «Моя идеальная свадьба»: info@expostatus.by\n"
                             "Региональные выставки:\n"
                             "Выставка в рамках областного фестиваля-ярмарки тружеников села «Дожинки-2022»: ves@brest-region.gov.by\n ")


        elif message.text == "Описание":
            bot.send_message(message.chat.id,
                             "Более подробную информацию вы можете узнать на нашем сайте: http://belarp.by/ru/calendar-of-events\n")

        elif message.text == "Место":
            bot.send_message(message.chat.id,
                             "Куда можно сходить в Минске и Минской области:\n"
                             "Кино: https://afisha.relax.by/kino/minsk/\n"
                             "Спектакли: https://afisha.relax.by/theatre/minsk/\n"
                             "Концерты: https://afisha.relax.by/conserts/minsk/\n "
                             "Спорт: https://afisha.relax.by/sport/minsk/\n"
                             "Выставки: https://afisha.relax.by/expo/minsk/\n")

        elif message.text == "Дата и время начало":
            bot.send_message(message.chat.id,
                             "Кино:\n"
                             "Спектакли:\n"
                             "Концерты: \n"
                             "Спорт:\n "
                             "Выставки:\n")

        elif message.text == "Стоимость входа":
            bot.send_message(message.chat.id,
                             "Кино:\n"
                             "Спектакли:\n"
                             "Концерты: \n"
                             "Спорт:\n "
                             "Выставки:\n")

        elif message.text == "Ссылка или телефон организатора":
            bot.send_message(message.chat.id,
                             "Связаться с организатором можно по ссылке:https://www.instagram.com/it_overone/\n")



        elif message.text == "Посмотреть событие города":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            town = types.KeyboardButton("Выбрать город")
            event = types.KeyboardButton("Запись о предстоящих событиях")
            back = types.KeyboardButton("Назад")
            markup.add(town, event, back)

            bot.send_message(message.chat.id, "Посмотреть событие города", reply_markup=markup)

        elif message.text == "Выбрать город":
            bot.send_message(message.chat.id,
                             "Заславль: https://www.calend.ru/travel/belorus/563/ \n"
                             "Боровляны: https://kolodischi.by/news/5868 \n"
                             "Сеница: https://realt.by/karty/poselki/senica/\n"
                             "Юбилейный: https://realt.by/karty/poselki/jubilejnyj/\n "
                             "Прилуки: https://www.calend.ru/travel/ukraine/1081/\n"
                             "Михановичи: https://belarus-tr.gazprom.ru/press/about-company/2022/01/473/\n"
                             "Мачулищи: https://eadaily.com/ru/news/2022/02/10/ucheniya-soyuznaya-reshimost-2022-nachalis-v-belorussii-sobytiya-nochi-10-fevralya\n"
                             "Гатово: https://realt.by/sale/flats/gatovo/\n"
                             "Ждановичи:https://bfla.eu/competition/events/eko-treyl-2022/ \n"
                             "Колодищи: https://kolodischi.by/\n"
                             "Березино: http://www.berezino.by/v-berezino-otkryvalas-ekspoziciya-posvyashhennaya-zhertvam-genocida/\n"
                             "Борисов: https://afisha.relax.by/conserts/borisov/\n"
                             "Жодино: https://zhodinonews.by/vse-novosti/\n"
                             "Копыль: https://www.calend.ru/travel/belorus/559/\n"
                             "Логойск: https://logoisk.by/novosti/\n"
                             "Любань: https://www.votpusk.ru/country/kurort.asp?CN=BEL&CT=BEL5\n"
                             "Марьина горка: http://www.region.by/news/ \n"
                             "Мядель: http://myadel.museum.by/\n"
                             "Фаниполь: http://ecopark.by/\n"
                             "Дзержинск: https://xn--80aiaefejqmp4ap.xn--p1ai/\n"
                             "Несвиж: https://niasvizh.by/sobytiya/season/\n"
                             "Слуцк: http://slutsk-gorod.by/ \n"
                             "Смолевичи: https://www.calend.ru/travel/belorus/648/ \n"
                             "Червень: http://www.cherven.by/afisha/\n"
                             "Осиповичи: http://osipinfo.by/ \n"
                             "Быхов: https://www.bykhov.by/\n"
                             "Горки: https://horki.info/afisha.html\n"
                             "Климовичи: https://mogilev-region.gov.by/category/kultura/znachimye-kulturnye-i-turisticheskie-sobytiya-na-2022-god\n"
                             "Кричев: https://www.calend.ru/travel/belorus/796/\n"
                             "Чериков: http://cherikov.gov.by/\n"
                             "Гродно: http://015.by/afisha/\n"
                             "Волковыск: https://volkovysknews.by/\n"
                             "Новогрудок: http://www.novogrudok.gov.by/uploads/files/2022.pdf\n"
                             "Речица: https://www.calend.ru/travel/belorus/641/\n"
                             "Рогачев: https://www.calend.ru/travel/belorus/843/\n"
                             "Поставы: https://postavy.vitebsk-region.gov.by/ru/meropriyatiya/\n")




        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_registration = types.KeyboardButton("Зарегистрировать событие")
            btn_Event_View = types.KeyboardButton("Посмотреть событие города")
            markup.add(btn_registration, btn_Event_View)
            bot.send_message(message.chat.id, "Назад", reply_markup=markup)
bot.polling(none_stop=True)