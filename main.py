from utils import load_json, decline_word, return_right, \
    return_wrong, return_coincidences
from class_players import Player

if __name__ == '__main__':

    player = Player(input('Введите ваше имя: '))
    word = load_json()

    print(f'{player}\n{word}')

    count = 0
    while len(player.used_words) != len(word.set_subwords):
        user_input = input('>: ').lower()

        if user_input in ('stop', 'стоп'):
            quit('Игра завершена!')

        elif player.checking_used_word(user_input):
            print(return_coincidences())

        elif word.checking_word(user_input):
            player.adding_word_to_used_words(user_input)
            count += 1
            print(return_right())

        elif user_input not in word.set_subwords or len(user_input) <= 2:
            print(return_wrong())

    print(f'Cлова закончились! Вы угадали {count} слов{decline_word(count)}'
          f' из {len(word.set_subwords)}\n')
