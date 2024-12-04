input = []
visited = set()
res = 0


with open('./input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        letters = list(line.split()[0])
        input.append(letters)

rows = len(input)
cols = len(input[0])
str = ["X","M","A","S"]
directions = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)]

def search(x, y, i, dx, dy):
    if i == 4:
        return 1
    nx, ny = x + dx, y + dy
    if (nx < 0 or ny < 0 or nx >= rows or ny >= cols or 
        input[nx][ny] != str[i]):
        return 0
    return search(nx, ny, i + 1, dx, dy)

res = 0
res2 = 0
for r in range(rows):
    for c in range(cols):
        if input[r][c] == 'X':
            for dx, dy in directions:
                res += search(r, c, 1, dx, dy)
# print(res)

def search_diag(x,y):
    if x <= 0 or y <= 0 or x >= rows - 1 or y >= rows - 1:
        return 0
    left = ("").join(sorted([input[x-1][y-1], input[x+1][y+1]]))
    right = ("").join(sorted([input[x-1][y+1],input[x+1][y-1]]))
    if left == "MS" and right == "MS":
        return 1
    return 0

for r in range(rows):
    for c in range(cols):
        if input[r][c] == 'A':
            res2 += search_diag(r,c)

print(res2)

# def search(x,y,i):
#     global res
#     if i > 3 or x < 0 or y < 0 or x >= rows or y >= cols or input[x][y] != str[i]:
#         return
#     if i == 3 and input[x][y] == "S":
#         res += 1
#         return
#     search(x,y-1,i+1)
#     search(x,y+1,i+1)
#     search(x-1,y,i+1)
#     search(x+1,y,i+1)
#     search(x-1,y-1,i+1)
#     search(x-1,y+1,i+1)
#     search(x+1,y-1,i+1)
#     search(x+1,y+1,i+1)

# for r in range(rows - 1):
#     for c in range(cols - 1):
#         search(r,c,0)

# print(res)

