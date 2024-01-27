import random
goodbuy = 0
while True:
    year = random.randint(1930, 1950)
    answer = input(">")

    if answer == "ПОКА!":
        goodbuy += 1

        if goodbuy == 3:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
            break
        else:
            print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
    else:
        goodbuy = 0
        if answer.isupper():
            print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
        else:
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")