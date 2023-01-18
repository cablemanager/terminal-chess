#!/usr/bin/env python3

from os import system

board = {
        'a1':'Ra1+','b1':'Nb1+','c1':'Bc1+','d1':'Qd1+','e1':'Ke1+','f1':'Bf1+','g1':'Ng1+','h1':'Rh1+',
        'a2':'a2+','b2':'b2+','c2':'c2+','d2':'d2+','e2':'e2+','f2':'f2+','g2':'g2+','h2':'h2+',
        'a3':'.','b3':'.','c3':'.','d3':'.','e3':'.','f3':'.','g3':'.','h3':'.',
        'a4':'.','b4':'.','c4':'.','d4':'.','e4':'.','f4':'.','g4':'.','h4':'.',
        'a5':'.','b5':'.','c5':'.','d5':'.','e5':'.','f5':'.','g5':'.','h5':'.',
        'a6':'.','b6':'.','c6':'.','d6':'.','e6':'.','f6':'.','g6':'.','h6':'.',
        'a7':'a7-','b7':'by-','c7':'c7-','d7':'d7-','e7':'e7-','f7':'f7-','g7':'g7-','h7':'h7-',
        'a8':'Ra8-','b8':'Nb8-','c8':'Bc8-','d8':'Qd8-','e8':'Ke8-','f8':'Bf8-','g8':'Ng8-','h8':'Rh8-'
        }

    #sample move: 

system('clear')

def white():
    return counter % 2 == 0

def isWP(piece):
    return ('-' in board[piece] or '.' in board[piece])

def isBP(piece):
    return ('+' in board[piece] or '.' in board[piece])

def corPiece(move):
    if 'O' in move:
        pass
    elif '-' in move:
        a = move.split('-')[0]
        b = move.split('-')[1]
    elif 'x' in move:
        a = move.split('x')[0]
    if not isPawn(a) and white() and board[a[1:]] == a + '+' and isWP(b):
        return True

    if isPawn(a) and white() and board[a] == a + '+' and isWP(b):
        return True

    elif not isPawn(a) and not white() and board[a[1:]] == a + '-' and isBP(b):
        return True

    elif isPawn(a) and not white() and board[a] == a + '-' and isBP(b):
        return True

    else:
        return False

def isPawn(piece):
    if len(piece) == 2:
        return True
    else:
        return False

def move(move):
    a = move.split('-')[0]
    b = move.split('-')[1]
    if white() and not isPawn(a):
        board[b] = a[0] + b  + '+'
    elif white() and isPawn(a):
        board[b] = b + '+'
    elif not white() and not isPawn(a):
        board[b] = a[0] + b + '-'
    else:
        board[b] = b + '-'
    if not isPawn(a):
        board[a[1:]] = '.'
    if isPawn(a):
        board[a] = '.'

def boardUI():
    print('\033[30m\033[47m  ________________  \033[0m')
    i = 8
    rows = 0
    while i > 0:
        collumn = '\033[30m\033[47m \u239f\033[0m'
        j = 'a'
        color = 0 + rows
        while j < 'i':
            if color % 2 == 0:
                bg = '\033[42m'
            else:
                bg = '\033[44m'
            #print(j + str(i))
            if board[j + str(i)] == '.':
                collumn += bg + '  \033[0m'

            elif board[j + str(i)][0] == 'K' and board[j + str(i)][-1] == '-':
                collumn += bg + '\u2654 \033[0m'

            elif board[j + str(i)][0] == 'K' and board[j + str(i)][-1] == '+':
                collumn += bg + '\u265A \033[0m'

            elif board[j + str(i)][0] == 'R' and board[j + str(i)][-1] == '-':
                collumn += bg + '\u2656 \033[0m'

            elif board[j + str(i)][0] == 'R' and board[j + str(i)][-1] == '+':
                collumn += bg + '\u265c \033[0m'

            elif board[j + str(i)][0] == 'B' and board[j + str(i)][-1] == '-':
                collumn += bg + '\u2657 \033[0m'

            elif board[j + str(i)][0] == 'B' and board[j + str(i)][-1] == '+':
                collumn += bg + '\u265d \033[0m'

            elif board[j + str(i)][0] == 'N' and board[j + str(i)][-1] == '-':
                collumn += bg + '\u2658 \033[0m'

            elif board[j + str(i)][0] == 'N' and board[j + str(i)][-1] == '+':
                collumn += bg + '\u265e \033[0m'

            elif board[j + str(i)][0] == 'Q' and board[j + str(i)][-1] == '-':
                collumn += bg + '\u2655 \033[0m'

            elif board[j + str(i)][0] == 'Q' and board[j + str(i)][-1] == '+':
                collumn += bg + '\u265B \033[0m'

            elif ord(board[j + str(i)][0]) in range(ord('a'),ord('i'),1) and board[j + str(i)][-1] == '-':
                collumn += bg + '\u2659 \033[0m'

            elif ord(board[j + str(i)][0]) in range(ord('a'),ord('i'),1) and board[j + str(i)][-1] == '+':
                collumn += bg + '\u265F \033[0m'
 
            else:
                collumn += '  '
            j = chr(ord(j) + 1)
            color += 1
        rows += 1
        print(collumn + '|')
        i -= 1
    print('\033[30m\033[47m   \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \033[0m')
counter = 0
running = True
boardUI()
while running:
    mv = input()
    if corPiece(mv):
        move(mv)
        counter += 1
        system('mpg321 move-self.mp3 2> /dev/null')
        system('clear')
        boardUI()
    else:
        print('Illegal')
