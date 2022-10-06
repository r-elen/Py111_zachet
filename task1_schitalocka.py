

SCET = ('Раз, два, три, четыре. Сосчитаем дыры')

        # Если в сыре много дыр, Значит, вкусным будет сыр.\
        # Если в нем одна дыра, Значит, вкусным был вчера.')

PEOPLE = ['Ваня', 'Катя', 'Петя']


def shet(text: str, people_list: list):
    words_list = text.split()

    winner_num = len(words_list) % len(people_list)

    if winner_num == 0:
        winner = people_list[-1]
    else:
        winner = people_list[winner_num-1]

    return winner_num, winner


if __name__ == '__main__':
    print(shet(SCET, PEOPLE))
