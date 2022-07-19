class Player:

    def __init__(self, user_name: str):
        """
        При инициализации экземпляру задаются: имя пользователя.
        """
        self.user_name = user_name
        # использованные слова пользователя
        self.used_words = []

    def __str__(self):
        """
        __repr__ - это однозначное представление объекта в виде строки, которое можно использовать,
        чтобы воссоздать точно такой же объект, или вывести какое-нибудь полезное сообщение.
        :return: Строку приветствия
        """
        return f'Привет,{self.user_name} !'

    def get_used_words(self) -> int:
        """
        Получает количество использованных слов.
        :return: int
        """
        return len(self.used_words)

    def checking_used_word(self, user_word) -> bool:
        """
        Проверяет использования данного слова до этого, если есть, то функция передаётся в
        adding_word_to_used_words и там обрабатывается
        :param user_word: пользовательский ввод.
        :return: булевое значение
        """
        return user_word in self.used_words

    def adding_word_to_used_words(self, user_word) -> None:
        """
        Добавление слова в использованные слова, делает проверку на то что пользователь
        ещё не использовал данное слово. И если не использовал, использует и
        потом добавляем его в список self.used_words = [].
        :param user_word: пользовательский ввод.
        :return: ничего не возвращает
        """
        if not self.checking_used_word(user_word):
            self.used_words.append(user_word)
