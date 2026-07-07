def count_xmas(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j].upper() == 'A':
                first_diag = False
                second_diag = False
                
                if i - 1 >= 0 and j - 1 >= 0 and i + 1 < rows and j + 1 < cols:
                    chars = {grid[i-1][j-1].upper(), grid[i+1][j+1].upper()}
                    if chars == {'M', 'S'}:
                        first_diag = True
                
                if i - 1 >= 0 and j + 1 < cols and i + 1 < rows and j - 1 >= 0:
                    chars = {grid[i-1][j+1].upper(), grid[i+1][j-1].upper()}
                    if chars == {'M', 'S'}:
                        second_diag = True
                
                if first_diag and second_diag:
                    count += 1
                    
    return count

f = open("input.txt", "r")
grid = [list(line.strip()) for line in f]
f.close()


print("Number of X-MAS patterns:", count_xmas(grid))
