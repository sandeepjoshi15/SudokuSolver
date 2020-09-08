board =  [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
#s = board name
#x,y are coordinates where operation is going on and pos = (x,y)
# num is number to be checked at position(x,y)
def print_board(s):
    for i in range(len(s)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(s[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(s[i][j])
            else:
                print(str(s[i][j]) + " ", end="")

def find_spaces(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j]==0:
                return(i,j)
    return None


def is_valid(s,pos,num):
    for i in range(len(s[0])): #checking all elements of row x i.e pos[0]
        if num==s[pos[0]][i] and i != pos[1]:
            return False
    for j in range(len(s)): #checking all elements of coloumn y i.e pos[1]
        if num==s[j][pos[1]] and j != pos[0]:
            return False
    for i in range(0,3):
        for j in range(0,3):
            box = (pos[0]//3,pos[1]//3)
            if num==s[box[0]*3+i][box[1]*3+j]:
                return False
    return True


def solve(s):
    #print (s)
    find = find_spaces(s)
    if not find:
        return True
    else:
        row,col = find #row and col are the position where zero is found.
    for i in range(1,10):
        if is_valid(s,(row,col),i):
            s[row][col] = i
            
            if solve(s):
                return True
            s[row][col] = 0

    return False
print('Given Sudoku')
print_board(board)
solve(board)
print('#######################\nSolved Sudoku')
print_board(board)












