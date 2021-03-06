import random


cuadros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
#cuadros = [int(1), int(2), int(3), int(4), int(5), int(6), int(7), int(8), int(9), int(10), int(11), int(12), int(13), int(14), int(15), int(16), int(17), int(18), int(19), int(20), int(21), int(22), int(23), int(24), int(25)]


def isBreakRow(dimension, actual):
    # Devuelve verdadero o falso dependiendo si se trata de una nueva fila
    if actual%dimension == 0: return True
    else: return False


def estadoJuego(tabla, dimension, pieza):
    revisados = []

    for i in range(1, len(tabla)):
        if tabla[i] == pieza and i not in revisados:
            # Revisión horizontal
            isRevisando = True
            revision = 1
            cont = i + 1
            while isRevisando:
                if tabla[cont] == pieza and not isBreakRow(dimension, (cont-1)):
                    revision += 1
                    revisados.append(cont)
                    cont += 1
                else:
                    isRevisando = False
            if revision >= 3:
                print(f'{pieza} gana!')


def crearTabla(dimension):
    tabla = []

    for i in range(0, (dimension * dimension) + 1):
        tabla.append(i)

    return tabla


def getBoardCopy(board):
    # Faz uma copia do quadro e retrona esta copia
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def drawBoard(board):
    # Esta función dibuja la tabla del juego
    copyBoard = getBoardCopy(board)
    divisor = '----------------------------'

    '''for i in range(1, 25):
        if (board[i] == ''):
            copyBoard[i] = str(i)
        else:
            copyBoard[i] = board[i]'''

    print(f' {copyBoard[1]}| {copyBoard[2]}| {copyBoard[3]}| {copyBoard[4]}| {copyBoard[5]}|')
    print(divisor)
    print(f' {copyBoard[6]}| {copyBoard[7]}| {copyBoard[8]}| {copyBoard[9]}|{copyBoard[10]}|')
    print(divisor)
    print(f'{copyBoard[11]}|{copyBoard[12]}|{copyBoard[13]}|{copyBoard[14]}|{copyBoard[15]}|')
    print(divisor)
    print(f'{copyBoard[16]}|{copyBoard[17]}|{copyBoard[18]}|{copyBoard[19]}|{copyBoard[20]}|')
    print(divisor)
    print(f'{copyBoard[21]}|{copyBoard[22]}|{copyBoard[23]}|{copyBoard[24]}|{copyBoard[25]}|')
    print(divisor)
    #print(f' {copyBoard[7]}')
    '''print(' ' + copyBoard[7] + '|' + copyBoard[8] + '|' + copyBoard[9])
    # print(' | |')
    print('-------')
    # print(' | |')
    print(' ' + copyBoard[4] + '|' + copyBoard[5] + '|' + copyBoard[6])
    # print(' | |')
    print('-------')
    # print(' | |')
    print(' ' + copyBoard[1] + '|' + copyBoard[2] + '|' + copyBoard[3])
    # print(' | |')
    print('-------')
    # print(' | |')'''


def inputPlayerLetter():
    # O jogador escolumnahe com qual letra ele quer jogar "X" ou "O"
    # Retorna uma lista com a letra do jogador e a letra do computador
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Escoge quien ser: X o O?')
        letter = input().upper()
        if (letter != 'X' and letter != 'O'):
            print("Escribe una letra X(xis) si quieres ser X u O(oh) si quieres ser O!")

    # O primeiro elemento na lista eh o do jogador e o segundo do computador
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirts():
    # Escolumnahe aleatoriamente o jogador que jogara primeiro
    if random.randint(0, 1) == 0:
        return 'computador'
    else:
        return 'jogador'


def makeMove(board, letter, move):
    # Faz o movimento do computador ou do jogador a depender do letter no quadro
    board[move] = letter


def isWinner(brd, let):
    # Dado um quadro e uma letra, esta funcao retorna True se a letra passada vence o jogo
    for i in range(1, len(brd)):
        revisadosH = []
        if i <= len(brd) and brd[i] == let and i not in revisadosH:
            # Revisión horizontal
            isRevisando = True
            revisionH = 1
            contH = i + 1
            while isRevisando:
                if brd[contH] != None and brd[contH] == let and not isBreakRow(5, (contH-1)):
                    revisionH += 1
                    revisadosH.append(contH)
                    contH += 1
                else:
                    isRevisando = False
            if revisionH >= 3:
                return True
        revisadosV = []
        if i <= len(brd) and brd[i] == let and i not in revisadosV:
            # Revisión vertical
            isRevisando = True
            revisionV = 1
            contV = i + 5
            while isRevisando:
                if brd[contV] != None and brd[contV] == let:
                    revisionV += 1
                    revisadosV.append(contV)
                    contV += 1
                else:
                    isRevisando = False
            if revisionV >= 3:
                return True
        revisadosD = []
        if i <= len(brd) and brd[i] == let and i not in revisadosD:
            # Revisión vertical
            isRevisando = True
            revisionD = 1
            contV = i + 6
            while isRevisando:
                if brd[contV] != None and brd[contV] == let:
                    revisionD += 1
                    revisadosD.append(contV)
                    contV += 1
                else:
                    isRevisando = False
            if revisionD >= 3:
                return True
    return False


def isSpaceFree(board, move):
    # Devuelve True si el espacio solicitado está libre
    if move in cuadros:
        return True
    else:
        return False


def getPlayerMove(board):
    # Recebe o movimento do jogador
    move = ''
    #while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
    while move not in cuadros or not isSpaceFree(board, int(move)):
        print('Cual es su próximo movimiento? (1-25)')
        move = input()
        if (move not in cuadros):
            print("MOVIMENTO INVALIDO! Escribe un número entre 1 y 25!")

        if (move in cuadros):
            if (not isSpaceFree(board, int(move))):
                print(
                    "Espacio inválido! Escoge otro espacio entre 1 y 25!")

    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # Retorna um movimento valido aleatorio
    # Retorna None se nao possui movimentos validos

    possiveisMovimentos = []
    for i in movesList:
        if isSpaceFree(board, i):
            possiveisMovimentos.append(i)

    if len(possiveisMovimentos) != 0:
        return random.choice(possiveisMovimentos)
    else:
        return None


def isBoardFull(board):
    # Retorna True se todos os espacos do quadro estao indisponiveis
    for i in range(1, 25):
        if isSpaceFree(board, i):
            return False
    return True


def possiveisOpcoes(board):
    # Retorna uma lista com todos os espacos no quadro que estao disponiveis

    opcoes = []

    for i in range(1, 25):
        if isSpaceFree(board, i):
            opcoes.append(i)

    return opcoes


def finishGame(board, computerLetter):
    # Verifica se o jogo chegou ao final
    # Retorna -1 se o jogador ganha
    # Retorna 1 se o computador ganha
    # Retorna 0 se o jogo termina empatado
    # Retorna None se o jogo nao terminou

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    if (isWinner(board, computerLetter)):
        return 1

    elif (isWinner(board, playerLetter)):
        return -1

    elif (isBoardFull(board)):
        return 0

    else:
        return None


def alphabeta(board, computerLetter, turn, alpha, beta):
    # Fazemos aqui a poda alphabeta

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    if turn == computerLetter:
        nextTurn = playerLetter
    else:
        nextTurn = computerLetter

    finish = finishGame(board, computerLetter)

    if (finish != None):
        return finish

    possiveis = possiveisOpcoes(board)

    if turn == computerLetter:
        for move in possiveis:
            makeMove(board, turn, move)
            val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
            makeMove(board, '', move)
            if val > alpha:
                alpha = val

            if alpha >= beta:
                return alpha
        return alpha

    else:
        for move in possiveis:
            makeMove(board, turn, move)
            val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
            makeMove(board, '', move)
            if val < beta:
                beta = val

            if alpha >= beta:
                return beta
        return beta


def getComputerMove(board, turn, computerLetter):
    # Definimos el movimiento de la IA

    a = -2
    opcoes = []

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # if len(possiveisOpcoes(board)) == 9:
    #   return 5

    # MiniMax
    # Primero revisa si puede ganar en el próximo movimiento
    for i in range(1, 26):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Revisa si el jugador gana en el siguiente movimiento y lo bloquea
    for i in range(1, 26):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    possiveisOpcoesOn = possiveisOpcoes(board)

    for move in possiveisOpcoesOn:

        makeMove(board, computerLetter, move)
        val = alphabeta(board, computerLetter, playerLetter, -2, 2)
        makeMove(board, '', move)

        if val > a:
            a = val
            opcoes = [move]

        elif val == a:
            opcoes.append(move)

    return random.choice(opcoes)


print('Tres en Raya!')

jogar = True

while jogar:
    # Reinicia el juego
    theBoard = crearTabla(5)
    print(theBoard)
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirts()
    print('El ' + turn + ' juega primero,')
    gameisPlaying = True

    while gameisPlaying:
        if turn == 'jogador':
            # turno del jugador
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Woooow! Ganaste!')
                gameisPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Empate!')
                    break
                else:
                    turn = 'computador'

        else:
            # Vez do computador
            move = getComputerMove(theBoard, playerLetter, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("La IA te ganó :(")
                gameisPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Empate!')
                    break
                else:
                    turn = 'jogador'

    letterNew = ''
    while not (letterNew == 'S' or letterNew == 'N'):
        print("Quieres jugar nuevamente? Escribe S(para si) o N(para no)")
        letterNew = input().upper()
        if (letterNew != 'S' and letterNew != 'N'):
            print("Entrada invalida! Escribe S(para si) o N(para no)!")
        if (letterNew == 'N'):
            print("Un gusto jugar contigo! Hasta la proxima!")
            jogar = False