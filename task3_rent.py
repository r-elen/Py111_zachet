
ZAYAVKI = [[12, 15], [18, 23], [15, 17], [6, 11], ]


def rocket(list_zayavok: list) -> bool:
    list_zayavok.sort()
    end_time = list_zayavok[0][1]

    dostup = True
    for i in range(len(list_zayavok)-1):
        start_time = list_zayavok[i+1][0]
        if end_time > start_time:
            dostup = False
        end_time = list_zayavok[i+1][1]

    return dostup


if __name__ == '__main__':
    print(rocket(ZAYAVKI))
