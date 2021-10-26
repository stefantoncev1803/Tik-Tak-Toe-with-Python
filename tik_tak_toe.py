array = [['0'] * 3 for i in range(3)]
array[0][0] = "1"
array[0][1] = "2"
array[0][2] = "3"
array[1][0] = "4"
array[1][1] = "5"
array[1][2] = "6"
array[2][0] = "7"
array[2][1] = "8"
array[2][2] = "9"

moves = 9


def print_board():
    print('''              --     --     --
             |{}|    |{}|    |{}|
              --     --     --
              --     --     --
             |{}|    |{}|    |{}|
              --     --     --
              --     --     --
             |{}|    |{}|    |{}|
              --     --     -- '''.format(array[0][0], array[0][1], array[0][2], array[1][0], array[1][1], array[1][2],
                                          array[2][0], array[2][1], array[2][2]))


def check_winner():
    if (array[0][0] == "X" and array[0][1] == "X" and array[0][2] == "X"):
        print("X wins!")
        return True
    elif (array[1][0] == "X" and array[1][1] == "X" and array[1][2] == "X"):
        print("X wins!")
        return True
    elif (array[2][0] == "X" and array[2][1] == "X" and array[2][2] == "X"):
        print("X wins!")
        return True
    elif (array[0][0] == "X" and array[1][0] == "X" and array[2][0] == "X"):
        print("X wins!")
        return True
    elif (array[0][1] == "X" and array[1][1] == "X" and array[2][1] == "X"):
        print("X wins!")
        return True
    elif (array[0][2] == "X" and array[1][2] == "X" and array[2][2] == "X"):
        print("X wins!")
        return True
    elif (array[0][0] == "X" and array[1][1] == "X" and array[2][2] == "X"):
        print("X wins!")
        return True
    elif (array[0][2] == "X" and array[1][1] == "X" and array[2][0] == "X"):
        print("X wins!")
        return True
    elif (array[0][0] == "O" and array[0][1] == "O" and array[0][2] == "O"):
        print("O wins!")
        return True
    elif (array[1][0] == "O" and array[1][1] == "O" and array[1][2] == "O"):
        print("O wins!")
        return True
    elif (array[2][0] == "O" and array[2][1] == "O" and array[2][2] == "O"):
        print("O wins!")
        return True
    elif (array[0][0] == "O" and array[1][0] == "O" and array[2][0] == "O"):
        print("O wins!")
        return True
    elif (array[0][1] == "O" and array[1][1] == "O" and array[2][1] == "O"):
        print("O wins!")
        return True
    elif (array[0][2] == "O" and array[1][2] == "O" and array[2][2] == "O"):
        print("O wins!")
        return True
    elif (array[0][0] == "O" and array[1][1] == "O" and array[2][2] == "O"):
        print("O wins!")
        return True
    elif (array[0][2] == "O" and array[1][1] == "O" and array[2][0] == "O"):
        print("O wins!")
        return True


print_board()

while True:

    hiks = input("Place x:(1-9)) ")

    if hiks != "1" and hiks != "2" and hiks != "3" and hiks != "4" and hiks != "5" and hiks != "6" and hiks != "7" and hiks != "8" and hiks != "9":
        print("Please enter valid number 1-9 ")

    elif hiks == "1":
        if array[0][0] == "X" or array[0][0] == "O":
            print("This field is already used! ")
            continue
        else:
            array[0][0] = "X"
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif hiks == "2":
        if array[0][1] == "X" or array[0][1] == "O":
            print("This field is already used! ")
            continue
        else:
            array[0][1] = 'X'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif hiks == "3":
        if array[0][2] == "X" or array[0][2] == "O":
            print("This field is already used! ")
            continue

        else:
            array[0][2] = 'X'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif hiks == "4":
        if array[1][0] == "X" or array[1][0] == "O":
            print("This field is already used! ")
            continue
        else:
            array[1][0] = 'X'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif hiks == "5":
        if array[1][1] == "X" or array[1][1] == "O":
            print("This field is already used! ")
            continue
        else:
            array[1][1] = 'X'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif hiks == "6":
        if array[1][2] == "X" or array[1][2] == "O":
            print("This field is already used! ")
            continue
        else:
            array[1][2] = 'X'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif hiks == "7":
        if array[2][0] == "X" or array[2][0] == "O":
            print("This field is already used! ")
            continue
        else:
            array[2][0] = 'X'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif hiks == "8":
        if array[2][1] == "X" or array[2][1] == "O":
            print("This field is already used! ")
            continue
        else:
            array[2][1] = 'X'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif hiks == "9":
        if array[2][2] == "X" or array[2][2] == "O":
            print("This field is already used! ")
            continue
        else:
            array[2][2] = 'X'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break

    ipsilon = input("Place O:(1-9)) ")
    if ipsilon != "1" and ipsilon != "2" and ipsilon != "3" and ipsilon != "4" and ipsilon != "5" and ipsilon != "6" and ipsilon != "7" and ipsilon != "8" and ipsilon != "9":
        print("Please enter valid number 1-9 ")

    elif ipsilon == "1":
        if array[0][0] == "X" or array[0][0] == "O":
            print("This field is already used! ")
            continue
        else:
            array[0][0] = "O"
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif ipsilon == "2":
        if array[0][1] == "X" or array[0][1] == "O":
            print("This field is already used! ")
            continue
        else:
            array[0][1] = 'O'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif ipsilon == "3":
        if array[0][2] == "X" or array[0][2] == "O":
            print("This field is already used! ")
            continue

        else:
            array[0][2] = 'O'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif ipsilon == "4":
        if array[1][0] == "X" or array[1][0] == "O":
            print("This field is already used! ")
            continue
        else:
            array[1][0] = 'O'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif ipsilon == "5":
        if array[1][1] == "X" or array[1][1] == "O":
            print("This field is already used! ")
            continue
        else:
            array[1][1] = 'O'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif ipsilon == "6":
        if array[1][2] == "X" or array[1][2] == "O":
            print("This field is already used! ")
            continue
        else:
            array[1][2] = 'O'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif ipsilon == "7":
        if array[2][0] == "X" or array[2][0] == "O":
            print("This field is already used! ")
            continue
        else:
            array[2][0] = 'O'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif ipsilon == "8":
        if array[2][1] == "X" or array[2][1] == "O":
            print("This field is already used! ")
            # continue
        else:
            array[2][1] = 'O'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    elif ipsilon == "9":
        if array[2][2] == "X" or array[2][2] == "O":
            print("This field is already used! ")
            continue
        else:
            array[2][2] = 'O'
            print_board()
            moves -= 1
            check_winner()
            if check_winner() == True:
                break
    print("moves are {} ".format(moves))
    if moves < 1:
        break
        print("It's a tie! ")