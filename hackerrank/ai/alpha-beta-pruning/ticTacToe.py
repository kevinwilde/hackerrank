#!/bin/python
# Minimax algorithm with alpha-beta pruning
# Choose middle box first if possible
import random

def vertWin(board, player):
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False

def horizWin(board, player):
    for i in range(3):
        if player == 'X' and board[i] == "XXX":
            return True
        elif player == "O" and board[i] == "OOO":
            return True
    return False

def diagWin(board, player):
    return board[1][1] == player and ((board[0][0] == player and board[2][2] == player) or (board[0][2] == player and board[2][0] == player))

def hasWon(board, player):
    return vertWin(board, player) or horizWin(board, player) or diagWin(board, player)

def boardFull(board):
    for i in range(3):
        if '_' in board[i]:
            return False
    return True

def actions(board, player):
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                actions.append((i, j, player))
    return actions

def result(board, action):
    from copy import deepcopy
    newBoard = deepcopy(board)
    newBoard[action[0]] = newBoard[action[0]][:action[1]] + action[2] + newBoard[action[0]][action[1]+1:]
    return newBoard

def done(board, depth):
    if hasWon(board, maxi):
        return 100-depth
    elif hasWon(board, mini):
        return 0+depth
    elif boardFull(board):
        return 50
    return -1
    
def maxVal(board, depth, alpha, beta):
    if done(board, depth) > 0:
        return done(board, depth)
    v = -1*float("inf")
    for action in actions(board, maxi):
        v = max(v, minVal(result(board, action), depth+1, alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v
        
def minVal(board, depth, alpha, beta):
    if done(board, depth) > 0:
        return done(board, depth)
    v = float("inf")
    for action in actions(board, mini):
        v = min(v, maxVal(result(board, action), depth+1, alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

# Complete the function below to print 2 integers separated by a single space which will be your next move 
def nextMove(board):
    if board[1][1] == '_':
        print 1, 1
    else:
        bestAction = None
        v = -1*float("inf")

        for action in actions(board, maxi):
            actionScore = minVal(result(board, action), 1, -1*float('inf'), float('inf'))

            if actionScore > v:
                v = actionScore
                bestAction = action

        print bestAction[0], bestAction[1]

#If player is X, I'm the first player.
#If player is O, I'm the second player.
maxi = raw_input()
if maxi == 'X':
    mini = 'O'
elif maxi == 'O':
    mini = 'X'

#Read the board now. The board is a 3x3 array filled with X, O or _.
oboard = []
for i in xrange(0, 3):
    oboard.append(raw_input())

nextMove(oboard)