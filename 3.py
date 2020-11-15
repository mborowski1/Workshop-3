def gra_w_zdadywanie_liczb_2():
    '''
    Number guessing game - computer tries to guess the number the player thinks about.
    :return: "You win!"
    '''
    print("Think about the number from 0 to 999 and I will need max. 10 attempts to quess it.")
    min = 0
    max = 1000

    while True:
        guess = int((max - min) / 2) + min
        while True:
            print("I guess:" + str(guess))
            answer = input("Was I right? Answer: too big, too small, You are right.")
            if answer == "You are right":
                return "I won!"
            elif answer == "too big":
                max = guess
                break
            elif answer == "too small":
                min = guess
                break
            else: print("do not cheat!")


print(gra_w_zdadywanie_liczb_2())
















    



























