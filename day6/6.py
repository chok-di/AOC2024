map = []

with open('./input.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        map.append(row)

direction = {"^":(-1,0),">":(0,1),"v":(1,0),"<":(0,-1)}
turn = {"^":">",">":"v","v":"<","<":"^"}

patrol = str
x,y = int,int
rows = len(map)
cols = len(map[1])

for r in range(rows):
    for c in range(cols):
        if map[r][c] in [">","v","<","^"]:
            patrol = map[r][c]
            x,y = r,c
            break

# used for part1
def run(x,y,patrol,count):
    map[x][y] = "X"
    while ((x in range(rows)) and (y in range(cols))):
        dx,dy = direction[patrol]
        if x + dx not in range(rows) or y + dy not in range(cols):
            return count
        if map[x+dx][y+dy] != "#":
            if map[x+dx][y+dy] != "X":
                map[x+dx][y+dy] = "X"
                count += 1
            x,y = x+dx, y+dy
            continue
        if map[x+dx][y+dy] == "#":
            patrol = turn[patrol]
            continue

# used for part2
def check_stuck(x,y,patrol):
    visited = set()
    while True:
        if (x,y,patrol) in visited:
            return True
        visited.add((x,y,patrol))
        dx,dy = direction[patrol]
        if x + dx not in range(rows) or y + dy not in range(cols):
            return False
        if map[x+dx][y+dy] != "#":
            x,y = x+dx, y+dy
            continue
        if map[x+dx][y+dy] == "#":
            patrol = turn[patrol]
            continue

#answer to part1
res1 = run(x,y,patrol,1)


#answer to part2
res2 = 0
for r in range(rows):
    for c in range(cols):
        if (r,c) != (x,y) and map[r][c] != "#":
            map[r][c] = "#"
            if check_stuck(x,y,patrol):
                res2 += 1
            map[r][c] = "."

print(res1)
print(res2)








