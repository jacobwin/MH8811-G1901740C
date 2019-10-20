
dictionanry={'0':'O','1':'X','2':' '}

def TicTacDraw(board):
    n=len(board)
    for i in range(n):
        s=' '
        for j in range(n):
            if j == (len(board[i])-1):
                s=s+dictionanry[str(board[i][j])]
            else:
                s=s+dictionanry[str(board[i][j])]+' | '
        if i == (len(board)-1):
            print(s)
        else:
            print(s)
            print('-'*(4*n-1))

    
    
    
 


