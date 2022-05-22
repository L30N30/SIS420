import random

cap = 26
dim = 5
celdas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']


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
    espacio = '-------------'

    for i in range(1, cap):
        if (board[i] == ''):
            copyBoard[i] = str(i)
        else:
            copyBoard[i] = board[i]

    print(' ' + copyBoard[21] + '|' + copyBoard[22] + '|' + copyBoard[23] + '|' + copyBoard[24] + '|' + copyBoard[25])
    print(espacio)
    print(' ' + copyBoard[16] + '|' + copyBoard[17] + '|' + copyBoard[18] + '|' + copyBoard[19] + '|' + copyBoard[20])
    print(espacio)
    print(' ' + copyBoard[11] + '|' + copyBoard[12] + '|' + copyBoard[13]+ '|' + copyBoard[14]+ '|' + copyBoard[15])
    print(espacio)
    print(' ' + copyBoard[6] + '| ' + copyBoard[7] + '| ' + copyBoard[8]+ '| ' + copyBoard[9]+ '|' + copyBoard[10])
    print(espacio)
    print(' ' + copyBoard[1] + '| ' + copyBoard[2] + '| ' + copyBoard[3]+ '| ' + copyBoard[4]+ '| ' + copyBoard[5])
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


def whoGoesFirts():
    # Escolumnahe aleatoriamente o jogador que jogara primeiro
    if random.randint(0, 1) == 0:
        return 'computador'
    else:
        return 'jogador'


def makeMove(board, letter, move):
    # Faz o movimento do computador ou do jogador a depender do letter no quadro
    board[move] = letter


def heuristica(brd, let, pos, min):
    copyBrd = getBoardCopy(brd)
    if revisionHorizontal(copyBrd, let, pos, min) or revisionVertical(copyBrd, let, pos, min) or revisionDiagonal(copyBrd, let, pos, min) or revisionDiagonalP(copyBrd, let, pos, min):
        return True
    else:
        return False


def revisionHorizontal(brd, let, pos, min):
    revisando = True
    piezas = 0
    cont = pos + 1
    while revisando:
        if (cont-1)%dim == 0 or cont > 25:
            revisando = False
            continue
        elif cont >= cap or cont < 0:
            revisando = False
            continue
        elif brd[cont] != let:
            revisando = False
            continue
        if cont < cap and (cont-1)%dim !=0 and brd[cont] == let:
            piezas += 1
        cont += 1
    if piezas > min: return True
    else: return False


def revisionVertical(brd, let, pos, min):
    revisando = True
    piezas = 0
    cont = pos + 5
    while revisando:
        if cont < cap:
            if cont > (cap-1):
                revisando = False
                continue
            elif brd[cont] != let:
                revisando = False
                continue
            elif brd[cont] == let:
                piezas += 1
            cont += 5
        else:
            revisando = False
            continue
    if piezas > min: return True
    else: return False


def revisionDiagonal(brd, let, pos, min):
    revisando = True
    piezas = 0
    cont = pos - (dim-1)
    while revisando:
        if cont < 0:
            if cont < 0:
                revisando = False
                continue
            elif brd[cont] != let:
                revisando = False
                continue
            if brd[cont] == let:
                piezas += 1
            cont -= (dim - 1)
        else:
            revisando = False
            continue
    if piezas > min: return True
    else: return False


def revisionDiagonalP(brd, let, pos, min):
    revisando = True
    piezas = 0
    cont = pos - (dim+1)
    while revisando:
        if cont >= cap or brd[cont] != let:
            revisando = False
            continue
        elif brd[cont] == let:
            piezas += 1
        cont -= (dim + 1)
    if piezas > min: return True
    else: return False


def isWinner(brd, let):
    # Dado um quadro e uma letra, esta funcao retorna True se a letra passada vence o jogo
    copyBrd = getBoardCopy(brd)
    for i in range(1, cap):
        if revisionHorizontal(copyBrd, let, i, 2) or revisionVertical(copyBrd, let, i, 2) or revisionDiagonal(copyBrd, let, i, 2) or revisionDiagonalP(copyBrd, let, i, 2):
            return True
    return False


def isSpaceFree(board, move):
    # Retorna true se o espaco solicitado esta livre no quadro
    if (board[move] == ''):
        return True
    else:
        return False


def getPlayerMove(board):
    # Recebe o movimento do jogador
    move = ''
    while move not in celdas or not isSpaceFree(board, int(move)):
        print('Qual eh o seu proximo movimento? (1-25)')
        move = input();
        if (move not in celdas):
            print("MOVIMENTO INVALIDO! INSIRA UM NUMERO ENTRE 1 E 25!")

        if (move in celdas):
            if (not isSpaceFree(board, int(move))):
                print(
                    "ESPACO INSDISPONIVEL! ESCOLHA OUTRO ESPACO ENTRE 1 E 25 O QUAL O NUMERO ESTA DISPONIVEL NO QUADRO!")

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
    for i in range(1, cap):
        if isSpaceFree(board, i):
            return False
    return True


def possiveisOpcoes(board):
    # Retorna uma lista com todos os espacos no quadro que estao disponiveis

    opcoes = []

    for i in range(1, cap):
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
    #print(possiveis)

    if turn == computerLetter:
        for move in possiveis:
            makeMove(board, turn, move)
            #if heuristica(board, computerLetter, possiveis[0], 1):
                #print('a')
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
                return i

    # Checa se o jogador pode vencer no proximo movimento e bloqueia
    for i in range(1, cap):
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


print('Vamos jogar jogo da velha!')

jogar = True

while jogar:
    # Reseta o jogo
    theBoard = [''] * ((dim*dim)+1)
    print(theBoard)
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirts()
    print('O ' + turn + ' joga primeiro,')
    gameisPlaying = True

    while gameisPlaying:
        if turn == 'jogador':
            # Vez do Jogador
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Woooow! Voce venceu o jogo!')
                gameisPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('O jogo terminou empatado')
                    break
                else:
                    turn = 'computador'

        else:
            # Vez do computador
            move = getComputerMove(theBoard, playerLetter, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("O computador venceu :(")
                gameisPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('O jogo terminou empatado')
                    break
                else:
                    turn = 'jogador'

    letterNew = ''
    while not (letterNew == 'S' or letterNew == 'N'):
        print("Voce quer jogar novamente? Digite S(para sim) ou N(para nao)")
        letterNew = input().upper()
        if (letterNew != 'S' and letterNew != 'N'):
            print("Entrada invalida! Digite S(para sim) ou N(para nao)!")
        if (letterNew == 'N'):
            print("Foi bom jogar com voce! Ate mais!")
            jogar = False