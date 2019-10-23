def TicTacDraw(board): 
    dict = {0:'O',1:'X',2:' '}
    n=len(board)
    for i in range(n):
        s=' '
        for b in range(n):
            if b !=n-1:
                s+= dict[board[i][b]]+' | '
            else:
                s+= dict[board[i][b]]
        print(s)
        if i!=n-1:
             print((4*n-1)*'-')

if __name__ == '__main__':
    board = [[0, 1, 2], [2, 0, 0], [1, 1, 2]]
    TicTacDraw(board)







    