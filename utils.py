from requests import get
from class_basic_word import BasicWord
from random import choice


def load_json(URL='https://jsonkeeper.com/b/T8Y6'):
    """
    Загружает по URL ссылке JSON файл, перемешивает данные,
    создаёт экземпляр класса BasicWord.
    :param URL: ссылка на данные
    :return: экземпляр класса BasicWord
    """

    # получит список слов с внешнего ресурса
    result = get(URL).json()
    # выбирает случайное слово для игры
    random = choice(result)

    for line in result:
        line['subwords'] = list(set(line['subwords']))

    word = BasicWord(random['word'], random['subwords'])
    return word


def decline_word(count: int) -> str:
    """
    Определяет конец слова: Например - 1 слово, 2 слова, 0 слов.
    :param count: Число "int"
    :return: str в зависимости от param: count
    """
    if count in [11, 12, 13, 14]:
        symbol = ''
    elif count % 10 == 1:
        symbol = 'о'
    elif count % 10 in [2, 3, 4]:
        symbol = 'а'
    else:
        symbol = ''
    return symbol


def return_right():
    """
    Возвращает случайное строковое значение из списка.
    :return: Случайную str.
    """
    return choice(["Верно!", "Отлично!", "Amazing!!!", "Так держать!", "Молодец!"])


def return_coincidences():
    """
    Возвращает случайное строковое значение из списка.
    :return: Случайную str.
    """
    return choice(["Это слово уже было!", "Ты уже его отгадывал!", "Уже есть в списке отгаданных"])


def return_wrong():
    """
    Возвращает случайное строковое значение из списка.
    :return: Случайную str.
    """
    return choice(["Мимо!", "Не верно!", "Не знаю такого слова", "Подумай ещё"])
