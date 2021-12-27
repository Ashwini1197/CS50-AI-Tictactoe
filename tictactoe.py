"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1
    if board == initial_state():
        return X
    if count % 2 != 0:
        return O
    else:
        return X
        

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i,j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action")
    tempboard = copy.deepcopy(board)
    tempboard[action[0]][action[1]] = player(board)
    return tempboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # rowwise winning possibility
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] ==X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None
    
    # column wise winning possibility
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:  
                return X
            elif board[0][j] == O:
                return O
            else:
                return None
    
    #diagonalwise winning possibility

    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O
    elif board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float('-inf')
    Min = float('inf')
    if player(board) == X:
        v,m = max_value(board, Max, Min)
        return m
    else:
        v,m = min_value(board,Max,Min)
        return m

def max_value(board,Max,Min):
    if terminal(board):
        return utility(board),None
    m = None
    v = float('-inf')
    for act in actions(board):
        aux = min_value(result(board,act),Max,Min)[0]
        Max = max(Max,aux)
        if aux > v:
            v = aux
            m = act
            if Max >= Min:
               break
    return [v,m]

def min_value(board,Max,Min):
    if terminal(board):
        return utility(board),None
    m = None
    v = float('inf')
    for act in actions(board):
        aux  = max_value(result(board,act),Max,Min)[0]
        Min = min(Min,aux)
        if aux < v:
            v = aux
            m = act
            if Max >= Min:
                break
    return [v,m]
