
define display_board(board):

print ('   |    | ')
print (' '+board[7]+' | '+ board[8]+' | '+ board[9])
print ('------------')
print (' '+board[4]+' | '+ board[5]+' | '+board[4])
print ('------------')
print (' '+board[3]+' | '+board[2]+' | '+board[1])
print ('  |    |  ')
board = [X]*10
display_board(board)
