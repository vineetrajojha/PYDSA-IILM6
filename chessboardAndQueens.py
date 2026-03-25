# problem link : https://cses.fi/problemset/task/1624/

#prototype


#def

def rIAM(grid, r,c):
    for i in range(8):
        if grid[r][i] == 'Q' or grid[i][c] == 'Q':
            return False

    for i in range(-7, 8):
        if r+i >= 0 and r+i < 8 and c+i >= 0 and c+i < 8 and grid[r+i][c+i] == 'Q':
            return False
        if r+i >= 0 and r+i < 8 and c-i >= 0 and c-i < 8 and grid[r+i][c-i] == 'Q':
            return False

    return True