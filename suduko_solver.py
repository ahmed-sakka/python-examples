def findNextCellToFill(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(grid, i, j, e):
        if all([e != grid[i][x] for x in range(9)]):
                if all([e != grid[x][j] for x in range(9)]):
                           # finding the top left x,y co-ordinates of the section containing the i,j cell
                            secTopX, secTopY = 3 * (i/3), 3 * (j/3)
                            for x in range(secTopX, secTopX+3):
                                    for y in range(secTopY, secTopY+3):
                                            if grid[x][y] == e:
                                                    return False
                                            return True
        return False

def solveSudoku(grid, i=0, j=0):
    #while True:
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                #break
                return True
        for e in range(1,10):
                if isValid(grid, i, j, e):
                        print "Writing", e, "to", "[", i, "]", "[", j, "]", "..."
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                            return True
                        grid[i][j] = 0
                        #break
        return False

if __name__ == "__main__":
    input = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
    solveSudoku(input)
    print input
