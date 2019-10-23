def TicTacDraw(board): 
    dict = {0:'O',1:'X',2:' '}
    n=len(board)
    for a in range(n):
        s=''
        for b in range(n):
            if board[a][b]==0:
                s+='o'
            elif board[a][b]==1:
                s+='x'
            elif board[a][b]==2:
                s+=' '
                if a>0:
                    print((4*n-1)*'-')
        str=' | '
        s=str.join(s)
        print(' '+s)

if __name__ == '__main__':
    board = [[0, 1, 2], [2, 0, 0], [1, 1, 2]]
    TicTacDraw(board)







    