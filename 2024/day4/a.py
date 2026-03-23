def isValid(x, y, sizeX, sizeY):
    return 0 <= x < sizeX and 0 <= y < sizeY


def findWordInDirection(grid, n, m, word, x, y, dirX, dirY):
    for index in range(len(word)):
        nx, ny = x + index * dirX, y + index * dirY
        if not isValid(nx, ny, n, m) or grid[nx][ny] != word[index]:
            return False
    return True


def searchWord(grid, word):
    count = 0
    n = len(grid)
    m = len(grid[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(n):
        for j in range(m):

            if grid[i][j] == word[0]:
                for dirX, dirY in directions:
                    if findWordInDirection(grid, n, m, word, i, j, dirX, dirY):
                        count += 1

    return count


with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f]

word = "XMAS"
result = searchWord(lines, word)
print(f"Number of occurrences of '{word}': {result}")
