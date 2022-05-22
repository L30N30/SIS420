import random


celdas_bloqueadas = ['4', '7', '17', '25']
celdas_bloqueadas_ai = [4, 7, 17, 25]
celdas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
cap = 26
dim = 5


def revisionHorizontal(brd, let, pos, det):
    piezas = 1
    increment = 1
    cont = pos + increment
    revisando = True

    while revisando:
        if ((cont-increment) % dim == 0) or (cont > (cap-1)):
            revisando = False
            continue
        else:
            if brd[cont] == let:
                piezas += 1
            else:
                revisando = False
                continue
        cont += increment

    if piezas >= det:
        return True
    else:
        return False


def revisionVertical(brd, let, pos, det):
    piezas = 1
    increment = 5
    cont = pos + increment
    revisando = True

    while revisando:
        if cont > (cap-1):
            revisando = False
            continue
        else:
            if brd[cont] == let:
                piezas += 1
            else:
                revisando = False
                continue
        cont += increment

    if piezas >= det:
        return True
    else:
        return False


def revisionDiagonal(brd, let, pos, det):
    piezas = 1
    increment = dim + 1
    cont = pos + increment
    revisando = True

    while revisando:
        if ((cont-increment) % dim == 0) or (cont > (cap-1)):
            revisando = False
            continue
        else:
            if brd[cont] == let:
                piezas += 1
            else:
                revisando = False
                continue
        cont += increment

    if piezas >= det:
        return True
    else:
        return False


def revisionDiagonalI(brd, let, pos, det):
    if (pos - 1) % dim == 0:
        return False

    piezas = 1
    increment = dim - 1
    cont = pos + increment
    revisando = True

    while revisando:
        if ((cont-increment-1) % dim == 0) or (cont > (cap-1)):
            revisando = False
            continue
        else:
            if brd[cont] == let:
                piezas += 1
            else:
                revisando = False
                continue
        cont += increment

    if piezas >= det:
        return True
    else:
        return False


def getBoardCopy(board):
    # Faz uma copia do quadro e retrona esta copia

    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def drawBoard(board):
    # Esta funcao imprime o quadro do jogo
    # O quadro eh uma lista de 9 strings representando o qaudro
    copyBoard = getBoardCopy(board)
    espacio = '----------------'

    for i in range(1, cap):
        if (board[i] == ''):
            if i > 9:
                copyBoard[i] = str(i)
            else:
                copyBoard[i] = f' {str(i)}'
        else:
            copyBoard[i] = f' {board[i]}'

    print(' ' + copyBoard[21] + '|' + copyBoard[22] + '|' + copyBoard[23] + '|' + copyBoard[24] + '|' + copyBoard[25])
    print(espacio)
    print(' ' + copyBoard[16] + '|' + copyBoard[17] + '|' + copyBoard[18] + '|' + copyBoard[19] + '|' + copyBoard[20])
    print(espacio)
    print(' ' + copyBoard[11] + '|' + copyBoard[12] + '|' + copyBoard[13] + '|' + copyBoard[14] + '|' + copyBoard[15])
    print(espacio)
    print(' ' + copyBoard[6] + '|' + copyBoard[7] + '|' + copyBoard[8] + '|' + copyBoard[9] + '|' + copyBoard[10])
    print(espacio)
    print(' ' + copyBoard[1] + '|' + copyBoard[2] + '|' + copyBoard[3] + '|' + copyBoard[4] + '|' + copyBoard[5])
    print(espacio)


def inputPlayerLetter():
    # O jogador escolumnahe com qual letra ele quer jogar "X" ou "O"
    # Retorna uma lista com a letra do jogador e a letra do computador
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Voce quer ser X ou O?')
        letter = input().upper()
        if (letter != 'X' and letter != 'O'):
            print("Entre apenas com a letra X(xis) se voce quer ser X ou com a letra O(oh) se voce quer ser O!")

    # O primeiro elemento na lista eh o do jogador e o segundo do computador
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Escolumnahe aleatoriamente o jogador que jogara primeiro
    if random.randint(0, 1) == 0:
        return 'computador'
    else:
        return 'jogador'


def makeMove(board, letter, move):
    # Faz o movimento do computador ou do jogador a depender do letter no quadro
    board[move] = letter


def isWinner(brd, let):
    winner = False

    copyBrd = getBoardCopy(brd)

    for i in range(1, cap):
        if brd[i] == let:
            if revisionHorizontal(copyBrd, let, i, 3) or revisionVertical(copyBrd, let, i, 3) or revisionDiagonal(copyBrd, let, i, 3) or revisionDiagonalI(copyBrd, let, i, 3):
                winner = True
                break

    return winner


def isSpaceFree(board, move):
    # Retorna true se o espaco solicitado esta livre no quadro
    if (board[move] == ''):
        return True
    else:
        return False


def getPlayerMove(board):
    # Recebe o movimento do jogador
    movimiento = ''
    while movimiento not in celdas or not isSpaceFree(board, int(movimiento)):
        print('Cual es su próximo movimiento? (1-25)')
        movimiento = input()
        if movimiento not in celdas:
            print("MOVIMIENTO INVALIDO! ESCRIBE UN NUMERO ENTRE 1 y 25!")
            continue

        if movimiento in celdas:
            if not isAvailableToPlay(board, 6) and movimiento in celdas_bloqueadas:
                movimiento = '26'
                print("ESPACIO NO DISPONIBLE! Espera a que queden seis espacios disponibles!")
                continue
            if not isSpaceFree(board, int(movimiento)):
                movimiento = '26'
                print("ESPACIO NO DISPONIBLE! ESCOJA OTRO ESPACIO ENTRE 1 y 25 U OTRO NÚMERO DEL TABLERO!")
                continue

    return int(movimiento)


def isAvailableToPlay(brd, num):
    copyBrd = getBoardCopy(brd)
    disponibles = 0
    for i in range(1, cap):
        if (copyBrd[i] == ''):
            disponibles += 1

    if disponibles <= num:
        return True
    else:
        return False


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
    for i in range(1, cap):
        if isSpaceFree(board, i):
            return False
    return True


def possiveisOpcoes(board, let):
    opciones = []
    brd = getBoardCopy(board)

    isPopulated = False
    for i in range(1, cap):
        if brd[i] == let:
            isPopulated = True

    if isPopulated:
        for i in range(1, cap):
            for j in range(1, 3):
                if brd[int(i)] == let:
                    if (int(i) + j) < cap:
                        if revisionHorizontal(brd, let, int(i), j) and not ((int(i) + (j - 1)) % dim == 0) and isSpaceFree(brd, int(i) + j):
                            opciones.append(int(i) + j)
                    if (int(i) + (j * 5)) < cap:
                        if revisionVertical(brd, let, int(i), j) and isSpaceFree(brd, int(i) + (j * 5)):
                            opciones.append(int(i) + (j * 5))
                    if (int(i) + (j * (dim + 1))) < cap:
                        if revisionDiagonal(brd, let, int(i), j) and not ((int(i) + (j * (dim + 1))) % dim == 0) and isSpaceFree(brd, int(i) + (j * (dim + 1))):
                            opciones.append(int(i) + (j * (dim + 1)))
                    if (int(i) + (j * (dim - 1))) < cap:
                        if revisionDiagonalI(brd, let, int(i), j) and not ((int(i) + (j * (dim - 1) - 1)) % dim == 0) and isSpaceFree(brd, int(i) + (j * (dim - 1))):
                            opciones.append(int(i) + (j * (dim - 1)))
    else:
        for i in range(1, cap):
            if isSpaceFree(brd, i):
                if not isAvailableToPlay(brd, 6) and not (i in celdas_bloqueadas_ai):
                    opciones.append(i)

    '''if len(opciones) != 0:
        for i in opciones:
            if not isAvailableToPlay(brd, 6) and (i in celdas_bloqueadas_ai):
                opciones.pop(opciones.index(i))'''

    return opciones


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

    possiveis = possiveisOpcoes(board, computerLetter)

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
    # Definimos aqui qual sera o movimento do computador

    a = -2
    opcoes = []

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # if len(possiveisOpcoes(board)) == 9:
    #   return 5

    # Comecamos aqui o MiniMax
    # Primeiro chechamos se podemos ganhar no proximo movimento
    for i in range(1, cap):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                if isAvailableToPlay(board, 6) and (i not in celdas_bloqueadas_ai):
                    return i

    # Checa se o jogador pode vencer no proximo movimento e bloqueia
    for i in range(1, cap):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                if isAvailableToPlay(board, 6) and (i not in celdas_bloqueadas_ai):
                    return i

    possiveisOpcoesOn = possiveisOpcoes(board, computerLetter)

    for move in possiveisOpcoesOn:

        makeMove(board, computerLetter, move)
        val = alphabeta(board, computerLetter, playerLetter, -2, 2)
        makeMove(board, '', move)

        if val > a:
            a = val
            opcoes = [move]

        elif val == a:
            opcoes.append(move)

    if len(opcoes) == 0:
        m = 0
        while len(opcoes) == 0:
            m = random.randint(1, 25)
            if m not in celdas_bloqueadas_ai:
                opcoes.append()
    return random.choice(opcoes)


print('Tres en raya!')

jogar = True

while jogar:
    # Reseta o jogo
    theBoard = [''] * 26
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('El ' + turn + ' juega primero,')
    gameisPlaying = True

    while gameisPlaying:
        if turn == 'jogador':
            # Vez do Jogador
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Woooow! Ganaste el juego!')
                gameisPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('EMPATE!')
                    break
                else:
                    turn = 'computador'

        else:
            # Vez do computador
            move = getComputerMove(theBoard, playerLetter, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("La IA ganó! :(")
                gameisPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('EMPATE!')
                    break
                else:
                    turn = 'jogador'

    letterNew = ''
    while not (letterNew == 'S' or letterNew == 'N'):
        print("Quieres jugar otra vez? Escribe S(para si) o N(para no)")
        letterNew = input().upper()
        if (letterNew != 'S' and letterNew != 'N'):
            print("Entrada invalida! Escribe S(para si) o N(para no)!")
        if (letterNew == 'N'):
            print("Un gusto jugar contigo! Hasta la proxima!")
            jogar = False