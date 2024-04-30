import asyncio
from textblob import TextBlob
from words_dictionary import Word
import requests
from aiogram import F
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram.types import FSInputFile

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7070904386:AAEuaRJlW7Gp7ECLerJi15qKT5mFh_BYVzc")
dp = Dispatcher()


# КОМАНДА START
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Информация о боте"),
            types.KeyboardButton(text="Выбрать предмет")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите действие"
    )
    await message.answer_sticker(sticker="https://raw.githubusercontent.com/DaryaKrv/homk/main/stik.webp")
    await message.answer("Привет!\nВыбери действие на клавиатуре", reply_markup=keyboard)


@dp.message(F.text.lower() == "выбрать предмет")
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Математика"),
            types.KeyboardButton(text="Русский язык"),
            types.KeyboardButton(text="Английский язык")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите предмет"
    )
    await message.answer("Выбери по какому предмету нужны справочные материалы", reply_markup=keyboard)


@dp.message(F.text.lower() == "информация о боте")
async def remind_me(message: types.Message):
    await message.reply("-БОТ ДЛЯ ПОДГОТОВКИ К ЭКЗАМЕНАМ-\n"
                        "Справочники по предметам:\n✦ Профильная и базовая математики\n✦ Русский язык"
                        "\n✦ Английский язык\nТакже:\n✶ Добавление слов в словарик\n✶ Отображение словаря"
                        "\n✶ Перевод слов\n✶ Проверяйте знания слов")


@dp.message(F.text.lower() == "математика")
async def alg(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Профиль"),
            types.KeyboardButton(text="База")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите уровень математики"
    )
    await message.answer("Какая именно?", reply_markup=keyboard)


@dp.message(F.text.lower() == "профиль")
async def alg_file(message: types.Message):
    await message.answer_photo(photo=FSInputFile("img/math_prev.png"))
    kb = [
        [
            types.KeyboardButton(text="Планиметрия"),
            types.KeyboardButton(text="Стереометрия"),
            types.KeyboardButton(text="Вероятность"),
            types.KeyboardButton(text="Векторы"),
            types.KeyboardButton(text="Тригонометрия")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Раздел/тема теории"
    )
    await message.answer("Выберите раздел", reply_markup=keyboard)


@dp.message(F.text.lower() == "вероятность")
async def math_file1(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/m-var.jpg'), caption="Математика - 11 класс - Вероятность "
                                                                           "\nДержи!")


@dp.message(F.text.lower() == "векторы")
async def math_file2(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/m-vect.jpg.'), caption="Математика - 11 класс - Векторы "
                                                                             "\nДержи!")


@dp.message(F.text.lower() == "планиметрия")
async def math_file3(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/m-plan.jpg'), caption="Математика - 11 класс - "
                                                                            "Планиметрия\nДержи!")


@dp.message(F.text.lower() == "стереометрия")
async def math_file4(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/m-stereo.jpg'), caption="Математика - 11 класс - "
                                                                              "Стереометрия\nДержи!")


@dp.message(F.text.lower() == "тригонометрия")
async def math_file5(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/m-trig.jpg'), caption="Математика - 11 класс - "
                                                                            "Тригонометрия\nДержи!")


@dp.message(F.text.lower() == "база")
async def alg_file6(message: types.Message):
    await message.answer_photo(photo=FSInputFile("img/math_prev.png"))
    await message.answer_document(document=FSInputFile('img/alg-baza.png'),
                                  caption="Математика - 11 класс - База\nДержи!")


@dp.message(F.text.lower() == "русский язык")
async def rus(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="1-3"),
            types.KeyboardButton(text="4"),
            types.KeyboardButton(text="5"),
            types.KeyboardButton(text="6"),
            types.KeyboardButton(text="7")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите номер задания..."
    )
    await message.answer("Выберите номер задания", reply_markup=keyboard)


@dp.message(F.text.lower() == "1-3")
async def rus_file1(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/rus-1_3.jpg'), caption="Русский язык - 11 класс - 1-3 "
                                                                             "задание\nДержи!")


@dp.message(F.text.lower() == "4")
async def rus_file2(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/rus-4.jpg'), caption="Русский язык - 11 класс - 4 "
                                                                           "задание\nДержи!")


@dp.message(F.text.lower() == "5")
async def rus_file3(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/rus_6.jpg'), caption="Русский язык - 11 класс - 5 "
                                                                           "задание\nДержи!")


@dp.message(F.text.lower() == "6")
async def rus_file4(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/rus-5.jpg'), caption="Русский язык - 11 класс - 6 "

                                                                           "задание (список плеоназмов)\nДержи!")


@dp.message(F.text.lower() == "7")
async def rus_file5(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/rus-7.jpg'), caption="Русский язык - 11 класс - 7 "
                                                                           "задание\nДержи!")


@dp.message(F.text.lower() == "английский язык")
async def alg(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Команды"),
            types.KeyboardButton(text="Словарь"),
            types.KeyboardButton(text="Перевод"),
            types.KeyboardButton(text="Теория для ЕГЭ")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="..."
    )
    await message.answer("Выберите раздел", reply_markup=keyboard)


@dp.message(F.text.lower() == "команды")
async def rus_file5(message: types.Message):
    await message.answer(text="Это раздел английского языка.\nДоступны:\n`/see_dict` - просмотреть словарь\n"
                              "`/dict` <слово на русском языке> - запись слова в словарь\n(автоматический "
                              "перевод слова на английский)\n`/say` <фраза или слово на русском языке> - "
                              "перевод на английский \n`/check` <фраза на рус. языке>/<эта же фраза на английском> - "
                              "проверка правильности вашего перевода\n`/translate` <фраза или слово на английском> - "
                              "перевод на русский язык\n`/orthography_check`  <слово> - проверка орфографии слова",
                         parse_mode="MARKDOWN")


@dp.message(F.text.lower() == "словарь")
async def rus_file5(message: types.Message):
    await message.answer(text="`/dict` <слово на русском языке> - запись слова в словарь\n`/see_dict` - просмотреть "
                              "словарь", parse_mode="MARKDOWN")


@dp.message(F.text.lower() == "перевод")
async def rus_file5(message: types.Message):
    await message.answer(text="`/say` <фраза или слово на русском языке> - "
                              "перевод на английский \n`/check` <фраза на рус. языке>/<эта же фраза на английском> - "
                              "проверка правильности вашего перевода\n`/translate` <фраза или слово на английском> - "
                              "перевод на русский язык \n`/orthography_check`  <слово> - проверка орфографии слова",
                         parse_mode="MARKDOWN")


@dp.message(F.text.lower() == "теория для егэ")
async def rus_file5(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Времена глаголов"),
            types.KeyboardButton(text="Таблица неправильных глаголов"),
            types.KeyboardButton(text="Фонетика"),
            types.KeyboardButton(text="Словообразование"),
            types.KeyboardButton(text="Синтаксис"),
            types.KeyboardButton(text="Косвенная речь")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите  раздел теории..."
    )
    await message.answer("Выберите раздел теории", reply_markup=keyboard)


@dp.message(F.text.lower() == "времена глаголов")
async def rus_file4(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/tenses_of_verbs.jpg'), caption="Английский язык - ЕГЭ - "
                                                                                     "Времена глаголов\nДержи!")


@dp.message(F.text.lower() == "таблица неправильных глаголов")
async def rus_file4(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/n_verbs.jpg'), caption="Английский язык - ЕГЭ - "
                                                                             "Неправильные глаголы\nДержи!")


@dp.message(F.text.lower() == "фонетика")
async def rus_file4(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/fonetika.jpg'), caption="Английский язык - ЕГЭ - "
                                                                              "Фонетика\nДержи!")


@dp.message(F.text.lower() == "словообразование")
async def rus_file4(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/slovoobr.jpg'), caption="Английский язык - ЕГЭ - "
                                                                              "Словообразование\nДержи!")


@dp.message(F.text.lower() == "синтаксис")
async def rus_file4(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/sintax.jpg'), caption="Английский язык - ЕГЭ - "
                                                                            "Синтаксис\nДержи!")


@dp.message(F.text.lower() == "косвенная речь")
async def rus_file4(message: types.Message):
    await message.answer_photo(photo=FSInputFile('img/kosv.jpg'), caption="Английский язык - ЕГЭ - "
                                                                          "Косвенная речь\nДержи!")


# КОМАНДА /orthography_check
@dp.message(Command("orthography_check"))
async def say_word(message: types.Message,
                   command: CommandObject
                   ):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return
    try:
        word = command.args
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды."
        )
        return
    line = word
    b = TextBlob(line)
    if line == str(b.correct()):
        await message.reply(text=f"Верно! {line} - корректно")
    else:
        await message.reply(text=f"Неверно! {str(b.correct())} - корректно, ваш ввод - {line}")


@dp.message(Command("say"))
async def say_word(message: types.Message,
                   command: CommandObject
                   ):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return
    try:
        word = command.args
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды."
        )
        return

    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": f"{word}",
        "target": "en",
        "source": "ru"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "2788f3fa2emsh0bad9d0955989d6p18f09ejsn5ce28541ba91",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    res = response.json()
    a = res["data"]['translations'][0]['translatedText']
    text = "Перевод: " + a
    await message.reply(text)


# КОМАНДА /translate <слово>
@dp.message(Command("translate"))
async def translate_word(message: types.Message,
                         command: CommandObject
                         ):
    # Если не переданы никакие аргументы, то
    # command.args будет None
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return
    try:
        word = command.args
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды."
        )
        return

    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": f"{word}",
        "target": "ru",
        "source": "en"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "2788f3fa2emsh0bad9d0955989d6p18f09ejsn5ce28541ba91",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    res = response.json()
    a = res["data"]['translations'][0]['translatedText']
    text = "Перевод: " + a
    await message.reply(text)


# КОМАНДА /check <слово>/<перевод слова>
@dp.message(Command("check"))
async def translate_word(message: types.Message,
                         command: CommandObject
                         ):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return
    try:
        text_to_transl, user_answ = command.args.split("/")
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды."
        )
        return

    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": f"{text_to_transl}",
        "target": "en",
        "source": "ru"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "2788f3fa2emsh0bad9d0955989d6p18f09ejsn5ce28541ba91",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    res = response.json()
    a = res["data"]['translations'][0]['translatedText']
    if a == user_answ:
        await message.reply("Верно!")
    else:
        await message.reply("Неверно:(")


# КОМАНДА /dict <слово>
@dp.message(Command("dict"))
async def add_word(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
    word_text = command.args

    if not word_text:
        await message.reply("Вы не ввели слово.")
        return
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": f"{word_text}",
        "target": "ru",
        "source": "en"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "2788f3fa2emsh0bad9d0955989d6p18f09ejsn5ce28541ba91",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    res = response.json()
    a = res["data"]['translations'][0]['translatedText']
    word = Word(word=word_text, translate=a)
    word.save()
    await message.reply(f"Слово '{word_text} - {a}' добавлено в словарь.")


# КОМАНДА /see_dict
@dp.message(Command("see_dict"))
async def see_dict(message: types.Message):
    words = Word.select()
    response = "----Соварь----\n"
    for word in words:
        response += f"{word.word} - {word.translate}\n--------------\n"
    await message.answer(response)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
