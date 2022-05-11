import random

# Alunos:
# Caique de Paula Figueiredo Coelho
# Lucas Queiroz


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

    for i in range(1, 10):
        if (board[i] == ''):
            copyBoard[i] = str(i)
        else:
            copyBoard[i] = board[i]

    print(' ' + copyBoard[7] + '|' + copyBoard[8] + '|' + copyBoard[9])
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
    # print(' | |')


def inputPlayerLetter():
    # O jogador escolumnahe com qual letra ele quer jogar "X" ou "O"
    # Retorna uma lista com a letra do jogador e a letra do computador
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Quieres ser X o O?')
        letter = input().upper()
        if (letter != 'X' and letter != 'O'):
            print("Entre apenas com a letra X(xis) se voce quer ser X ou com a letra O(oh) se voce quer ser O!")

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
    return ((brd[7] == let and brd[8] == let and brd[9] == let) or  # linha de cima
            (brd[4] == let and brd[5] == let and brd[6] == let) or  # linha do meio
            (brd[1] == let and brd[2] == let and brd[3] == let) or  # linha de baixo
            (brd[7] == let and brd[4] == let and brd[1] == let) or  # columnauna da esquerda
            (brd[8] == let and brd[5] == let and brd[2] == let) or  # columnauna do meio
            (brd[9] == let and brd[6] == let and brd[3] == let) or  # columnauna da direito
            (brd[7] == let and brd[5] == let and brd[3] == let) or  # diagonal principal
            (brd[9] == let and brd[5] == let and brd[1] == let))  # diagonal secundaria


def isSpaceFree(board, move):
    # Retorna true se o espaco solicitado esta livre no quadro
    if (board[move] == ''):
        return True
    else:
        return False


def getPlayerMove(board):
    # Recebe o movimento do jogador
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Qual eh o seu proximo movimento? (1-9)')
        move = input();
        if (move not in '1 2 3 4 5 6 7 8 9'):
            print("MOVIMENTO INVALIDO! INSIRA UM NUMERO ENTRE 1 E 9!")

        if (move in '1 2 3 4 5 6 7 8 9'):
            if (not isSpaceFree(board, int(move))):
                print(
                    "ESPACO INSDISPONIVEL! ESCOLHA OUTRO ESPACO ENTRE 1 E 9 O QUAL O NUMERO ESTA DISPONIVEL NO QUADRO!")

        copy = getBoardCopy(board)
        makeMove(copy, playerLetter, 5)

        if int(move) == 5 and not isWinner(copy, playerLetter):
            print('Jugada invalida!')
            move = ''

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
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


def possiveisOpcoes(board):
    # Retorna uma lista com todos os espacos no quadro que estao disponiveis

    opcoes = []

    for i in range(1, 10):
        copy = getBoardCopy(board)
        makeMove(copy, computerLetter, i)
        if isSpaceFree(board, i):
            if i == 5 and isWinner(copy, computerLetter):
                opcoes.append(i)
            elif i != 5:
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
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i) and i != 5:
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
        elif i == 5:
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Checa se o jogador pode vencer no proximo movimento e bloqueia
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if i == 5:
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                print('Compu perdió!')
                continue
        else:
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


print('Vamos a jugar Tres en Raya!')

jogar = True

while jogar:
    # Reseta o jogo
    theBoard = [''] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirts()
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
                print("Perdiste :(")
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
        print("Jugar otra vez? Escribe S(para si) o N(para no)")
        letterNew = input().upper()
        if (letterNew != 'S' and letterNew != 'N'):
            print("Entrada invalida! Escribe S(para si) o N(para no)")
        if (letterNew == 'N'):
            print("Un gusto jugar contigo! Hasta luego!")
            jogar = False