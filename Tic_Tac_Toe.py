def TIC_():
    def player():
        cro_cir = ['X', 'O']
        player1 = input("Please pick a marker 'X' or 'O': ")
        while player1 != 'X' and player1 != 'O':
            player1 = input('Please enter \'X\'or \'O\': ')
        cro_cir.pop(cro_cir.index(player1))
        player2 = cro_cir[0]
        return player1, player2

    def board_fun(loc):
        board = {1: '   |   |   ', 2: ' | ', 3: '-' * 12}
        l = [1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1]
        ini = 1
        for i in l:
            if i == 2:
                print(' ' + str(loc[ini - 1]) + board[2] + str(loc[ini]) + board[2] + str(loc[ini + 1]) + ' ')
                ini += 3
            else:
                print(board[i])

    def control_fun(x_r, p1, p2):
        l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for i in l:
            if x_r[i[0] - 1] == x_r[i[1] - 1] == x_r[i[2] - 1] == p1:
                return False, 1
            elif x_r[i[0] - 1] == x_r[i[1] - 1] == x_r[i[2] - 1] == p2:
                return False, 2
        return True, 3

    def input_fun(player):
        while True:
            try:
                input_ = int(input('{} goes first.(input a number 1-9): '.format(player)))
                break
            except ValueError:
                print('Please enter a number 1-9+')
        while True:
            if 0 < input_ < 10:
                return input_
                break
            else:
                print('Please enter a number 1-9')
                input_ = int(input('Player 1 goes first.(input a number 1-9): '))

    x_r = [' ' for i in range(9)]
    player1, player2 = player()
    x = list(range(1, 10))
    board_fun(x)
    input1 = input_fun("player1")
    x_r.insert(input1 - 1, player1)
    x_r.pop(input1)
    board_fun(loc=x_r)

    while True:
        while True:
            input2 = input_fun("player2")
            if x_r[input2 - 1] == ' ':
                x_r.insert(input2 - 1, player2)
                x_r.pop(input2)
                board_fun(loc=x_r)
                break
            else:
                print('There is already occupied.Please enter another number(input a number 1-9): ')

        if control_fun(x_r, player1, player2)[1] == 2:
            print('player 2 wins !')
            break

        while True:
            input1 = input_fun("player1")
            if x_r[input1 - 1] == ' ':
                x_r.insert(input1 - 1, player1)
                x_r.pop(input1)
                board_fun(loc=x_r)
                break
            else:
                print('There is already occupyed.Please enter another number(input a number 1-9): ')
        if control_fun(x_r, player1, player2)[1] == 1:
            print('player 1 wins !')
            break

        if ' ' not in x_r:
            print('Tie')
            break