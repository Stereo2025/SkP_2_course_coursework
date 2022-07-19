class BasicWord:

    def __init__(self, original_word: str, set_subwords: list):
        """
        При инициализации экземпляру задаются: исходное слово и набор допустимых подслов
        """
        # исходное слово
        self.original_word = original_word
        # набор допустимых подслов
        self.set_subwords = set_subwords

    def __str__(self) -> str:
        """
        __repr__ - это однозначное представление объекта в виде строки, которое можно использовать,
        чтобы воссоздать точно такой же объект, или вывести какое-нибудь полезное сообщение.
        :return: Строку с данными согласно ТЗ.
        """
        return f'Составьте {self.counting_word()} слов из слова {self.original_word.upper()}\n' \
               f'Слова должны быть не короче 3 букв\n' \
               f'Чтобы закончить игру, угадайте все слова или напишите "stop или стоп"\n' \
               f'Поехали, ваше первое слово?'

    def checking_word(self, user_input) -> bool:
        """
        Проверяет введенное слова в списке допустимых подслов.
        :param user_input: пользовательский ввод
        :return: булевое значение
        """
        return user_input in self.set_subwords

    def counting_word(self) -> int:
        """
        Подсчитывает количество подслов в списке.
        :return: int
        """
        return len(self.set_subwords)
