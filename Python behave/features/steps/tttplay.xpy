from tictactoe import EMPTY_BOARD, play, play_best_move
from behave import *

# board = EMPTY_BOARD # clear the 3 x 3 tictactoe board
# winner = None   # set winner to none

# board, winner = play(board, 'X', 1,1)   # take middle position
# board, winner = play_best_move(board, 'O')

# if board[6] == None:
#     board, winner = play(board, 'X', 0,2)   # take bottom left
# else:
#     board, winner = play(board, 'X', 2, 2)  # take bottom right

# assert board[4] == 'X'  # test if the middle position is taken by X

@given('we have an empty tic-tac-toe board')
def step_impl(context):
    context.board = EMPTY_BOARD
    context.winner = None

@when(u'I play X on column {column} and row {row} on the board')
def step_impl(context,column,row):
    col = int(column) - 1
    row = int(row) - 1
    context.board, context.winner = play(context.board, 'X', col, row)

@when('I ask the computer to do its best move for O')
def step_impl(context):
    context.board, context.winner = play_best_move(context.board, 'O')

@then(u'the board has a O in column {column} and row {row} on the board')
def step_impl(context,column,row):
    col = int(column) - 1
    ro = int(row) - 1
    pos_on_board = 3*ro + col
    assert context.board[pos_on_board] == 'O'




@given('we have an empty tic-tac-toe bord')
def step_impl(context):
    context.board = EMPTY_BOARD
    context.winner = None

# @when('I play X on column 2 and row 2 on the board')
# def step_impl(context):
#     col = 2 - 1
#     row = 2 - 1
#     context.board, context.winner = play(context.board, 'X', col, row)

# @when('I ask the computer to do its best move for O')
# def step_impl(context):
#     context.board, context.winner = play_best_move(context.board, 'O')

# @when('I play X on column 2 and row 3 on the board')
# def step_impl(context):
#     col = 2 - 1
#     row = 3 - 1
#     context.board, context.winner = play(context.board, 'X', col, row)

# @when('I ask the computer to do its best move for O')
# def step_impl(context):
#     context.board, context.winner = play_best_move(context.board, 'O')

# @when('I play X on column 1 and row 3 on the board')
# def step_impl(context):
#     col = 1 - 1
#     row = 3 - 1
#     context.board, context.winner = play(context.board, 'X', col, row)

# @when('I ask the computer to do its best move for O ')
# def step_impl(context):
#     context.board, context.winner = play_best_move(context.board, 'O')

@then('O is the winner of the game')
def step_impl(context):
    assert context.winner == 'O'