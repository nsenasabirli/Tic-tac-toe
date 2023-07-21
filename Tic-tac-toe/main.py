import random

print('*****Welcome*****')

gameover = False  ##When the game is done, we shall set this value to true.
yourturn = True  ##We utilized it to determine if it was the player's turn.
ai = False  ##We utilized it to determine whether or not the rank is in artificial intelligence.
scoreless = False  ##When the game finishes in a tie, we will do True and the game will be over.

line1 = ['-', '-', '-']  ##We organized the game's locations into three lists, or lines.
line2 = ['-', '-', '-']
line3 = ['-', '-', '-']

l1 = [0, 0, 0]
l2 = [0, 0, 0]  ##WE WILL COMPLETE ALL OPERATIONS VIA THIS LIST.
l3 = [0, 0, 0]  ##EACH 'O' MARK IS 3 POINTS, WHILE EACH 'X' MARK IS 5 POINTS.


def result():  ##The rows are printed using the result function. Naturally, it depicts the game's end condition.
    print(line1)
    print(line2)
    print(line3)
    print('---------')


def control():  ##The control function, on the other hand, determines whether the game is finished when the movements are completed.
    global gameover, a, b, c, d, e, f, g, h, scoreless
    a = int(l1[0] + l1[1] + l1[2])  ##first line sum
    b = int(l2[0] + l2[1] + l2[2])  ##second line sum
    c = int(l3[0] + l3[1] + l3[2])  ##third line sum
    d = int(l1[0] + l2[0] + l3[0])  ##first column sum
    e = int(l1[1] + l2[1] + l3[1])  ##second column sum
    f = int(l1[2] + l2[2] + l3[2])  ##third column sum
    g = int(l1[0] + l2[1] + l3[2])  ##cross sum
    h = int(l1[2] + l2[1] + l3[0])  ##second cross sum
    if a == 9 or b == 9 or c == 9 or d == 9 or e == 9 or f == 9 or g == 9 or h == 9:
        gameover = True  ##If any of the values above is 9, 'O,' the player wins. The game is over.
        print('You Won!!!')
    elif a == 15 or b == 15 or c == 15 or d == 15 or e == 15 or f == 15 or g == 15 or h == 15:
        gameover = True  ##If the total is 15, the computer wins since the numbers are 5-5-5.
        print('You failed :(')
    elif (a + b + c) == 35:
        if scoreless == False:  ##If neither side wins, the total number of columns will be 35. (because the player started it)
            gameover = True
            print('Scoreless!')
            scoreless = True  ##This variable's purpose is to print text on the screen just once.


def artificial():
    global yourturn, ai, line1, line2, line3, sar, sur, a, b, c, d, e, f, g, h, l1, l2, l3
    ai = False ##Following the move, the turn will be transferred from artificial intelligence to the player.
    yourturn = True

    if gameover == False:  ##If the game is not completed, a loop is executed.
        if a == 10:  ##If a is 10, it puts x in the blank.
            if l1[0] == 0:  ##Scans the empty part
                l1[0] = 5
                line1[0] = 'X'
                result()

            elif l1[1] == 0:  ##SCans the empty part
                l1[1] = 5
                line1[1] = 'X'
                result()
            elif l1[2] == 0:  ##Scans the empty part
                l1[2] = 5
                line1[2] = 'X'
                result()

        elif b == 10:
            if l2[0] == 0:
                l2[0] = 5
                line2[0] = 'X'
                result()
            elif l2[1] == 0:
                l2[1] = 5
                line2[1] = 'X'
                result()
            elif l2[2] == 0:
                l2[2] = 5
                line2[2] = 'X'
                result()

        elif c == 10:
            if l3[0] == 0:
                l3[0] = 5
                line3[0] = 'X'
                result()
            elif l3[1] == 0:
                l3[1] = 5
                line3[1] = 'X'
                result()
            elif l3[2] == 0:
                l3[2] = 5
                line3[2] = 'X'
                result()

        elif d == 10:
            if l1[0] == 0:
                l1[0] = 5
                line1[0] = 'X'
                result()
            elif l2[0] == 0:
                l2[0] = 5
                line2[0] = 'X'
                result()
            elif l3[0] == 0:
                l3[0] = 5
                line3[0] = 'X'
                result()

        elif e == 10:
            if l1[1] == 0:
                l1[1] = 5
                line1[1] = 'X'
                result()
            elif l2[1] == 0:
                l2[1] = 5
                line2[1] = 'X'
                result()
            elif l3[1] == 0:
                l3[1] = 5
                line3[1] = 'X'
                result()

        elif f == 10:
            if l1[2] == 0:
                l1[2] = 5
                line1[2] = 'X'
                result()
            elif l2[2] == 0:
                l2[2] = 5
                line2[2] = 'X'
                result()
            elif l3[2] == 0:
                l3[2] = 5
                line3[2] = 'X'
                result()

        elif g == 10:
            if l1[0] == 0:
                l1[0] = 5
                line1[0] = 'X'
                result()
            elif l2[1] == 0:
                l2[1] = 5
                line2[1] = 'X'
                result()
            elif l3[2] == 0:
                l3[2] = 5
                line3[2] = 'X'
                result()

        elif h == 10:
            if l1[2] == 0:
                l1[2] = 5
                line1[2] = 'X'
                result()
            elif l2[1] == 0:
                l2[1] = 5
                line2[1] = 'X'
                result()
            elif l3[0] == 0:
                l3[0] = 5
                line3[0] = 'X'
                result()



        elif a == 6:  ##If the value is 6, it defends by inserting an X into the blank.

            if l1[0] == 0:  ##to check for an empty section
                l1[0] = 5
                line1[0] = 'X'
                result()
            elif l1[1] == 0:  ##to check for an empty section
                l1[1] = 5
                line1[1] = 'X'
                result()
            elif l1[2] == 0:  ##to check for an empty section
                l1[2] = 5
                line1[2] = 'X'
                result()

        elif b == 6:
            if l2[0] == 0:
                l2[0] = 5
                line2[0] = 'X'
                result()
            elif l2[1] == 0:
                l2[1] = 5
                line2[1] = 'X'
                result()
            elif l2[2] == 0:
                l2[2] = 5
                line2[2] = 'X'
                result()

        elif c == 6:
            if l3[0] == 0:
                l3[0] = 5
                line3[0] = 'X'
                result()
            elif l3[1] == 0:
                l3[1] = 5
                line3[1] = 'X'
                result()
            elif l3[2] == 0:
                l3[2] = 5
                line3[2] = 'X'
                result()

        elif d == 6:
            if l1[0] == 0:
                l1[0] = 5
                line1[0] = 'X'
                result()
            elif l2[0] == 0:
                l2[0] = 5
                line2[0] = 'X'
                result()
            elif l3[0] == 0:
                l3[0] = 5
                line3[0] = 'X'
                result()

        elif e == 6:
            if l1[1] == 0:
                l1[1] = 5
                line1[1] = 'X'
                result()
            elif l2[1] == 0:
                l2[1] = 5
                line2[1] = 'X'
                result()
            elif l3[1] == 0:
                l3[1] = 5
                line3[1] = 'X'
                result()

        elif f == 6:
            if l1[2] == 0:
                l1[2] = 5
                line1[2] = 'X'
                result()
            elif l2[2] == 0:
                l2[2] = 5
                line2[2] = 'X'
                result()
            elif l3[2] == 0:
                l3[2] = 5
                line3[2] = 'X'
                result()

        elif g == 6:
            if l1[0] == 0:
                l1[0] = 5
                line1[0] = 'X'
                result()
            elif l2[1] == 0:
                l2[1] = 5
                line2[1] = 'X'
                result()
            elif l3[2] == 0:
                l3[2] = 5
                line3[2] = 'X'
                result()

        elif h == 6:
            if l1[2] == 0:
                l1[2] = 5
                line1[2] = 'X'
                result()
            elif l2[1] == 0:
                l2[1] = 5
                line2[1] = 'X'
                result()
            elif l3[0] == 0:
                l3[0] = 5
                line3[0] = 'X'
                result()


        else:
            if l2[1] == 0:  ##If the center section is left blank, the chances of winning X bets improve.
                l2[1] = 5
                line2[1] = 'X'
                result()
            else:  ##If the middle section is crowded, the chances of winning the corners improve. It accomplishes this by producing random values.
                sar = random.randint(1, 3)
                sur = random.randint(1, 3)
                sur -= 1
                if sar == 2 or sur == 1:
                    artificial()
                else:
                    if sar == 1:
                        if line1[sur] == 'X' or line1[sur] == 'O':
                            artificial()
                        else:
                            line1[sur] = 'X'
                            l1[sur] = 5
                            result()
                    elif sar == 2:
                        if line2[sur] == 'X' or line2[sur] == 'O':
                            artificial()
                        else:
                            line2[sur] = 'X'
                            l2[sur] = 5
                            result()
                    elif sar == 3:
                        if line3[sur] == 'X' or line3[sur] == 'O':
                            artificial()
                        else:
                            line3[sur] = 'X'
                            l3[sur] = 5
                            result()
        control()

    if gameover == False:  ##prints the result and invokes the control function
        wish()


def wish():
    name = input()

    if name == '1' or name == '2' or name == '3' or name == '4' or name == '5' or name == '6' or name == '7' or name == '8' or name == '9':

        global yourturn
        global ai
        yourturn = False
        ai = True

        if name == '1':
            if line1[0] == 'O' or line1[0] == 'X':
                print('Please choose an empty place!!!')
                wish()
            else:
                line1[0] = 'O'
                l1[0] = 3
                result()
                control()

        elif name == '2':
            if line1[1] == 'O' or line1[1] == 'X':
                print('Please choose an empty place!!!')
                wish()
            else:
                line1[1] = 'O'
                l1[1] = 3
                result()
                control()
        elif name == '3':
            if line1[2] == 'O' or line1[2] == 'X':
                print('Please choose an empty place!!!')
                wish()
            else:
                line1[2] = 'O'
                l1[2] = 3
                result()
                control()
        elif name == '4':
            if line2[0] == 'O' or line2[0] == 'X':
                print('Please choose an empty place!!!')
                wish()
            else:
                line2[0] = 'O'
                l2[0] = 3
                result()
                control()
        elif name == '5':
            if line2[1] == 'O' or line2[1] == 'X':
                print('Please choose an empty place!!!')
                wish()
            else:
                line2[1] = 'O'
                l2[1] = 3
                result()
                control()
        elif name == '6':
            if line2[2] == 'O' or line2[2] == 'X':
                print('Please choose an empty place!!!')
                wish()
            else:
                line2[2] = 'O'
                l2[2] = 3
                result()
                control()
        elif name == '7':
            if line3[0] == 'O' or line3[0] == 'X':
                print('Please choose an empty place!!!')
                wish()
            else:
                line3[0] = 'O'
                l3[0] = 3
                result()
                control()
        elif name == '8':
            if line3[1] == 'O' or line3[1] == 'X':
                print('Please choose an empty place!!!')
                wish()
            else:
                line3[1] = 'O'
                l3[1] = 3
                result()
                control()
        elif name == '9':
            if line3[2] == 'O' or line3[2] == 'X':
                print('Please choose an empty place!!!')
                wish()
            else:
                line3[2] = 'O'
                l3[2] = 3
                result()
                control()
    else:
        print('Wrong Key')
        wish()

    if gameover == False:
        artificial()


result()

print('Your Turn (O)')

wish()

print('Game Over')
print("""Prepared by:
    Kerem Kahraman
    Necati Buğra Bebe
    Elif Naz Kadayıfçı
    Nahide Sena Sabırlı""")
