with open("input.txt", "r") as f:
    paths = f.readlines()
    paths = [line.strip() for line in paths]

#FIRST HALF

trees=0
r, c = 0, 0
while True:
    c+=3
    r+=1
    if r>=len(paths):
        break
    else:
        if paths[r][c % len(paths[r])] == "#":
            trees+=1

print(trees)

#SECOND HALF

total_trees=1
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
for slope in slopes:
    trees=0
    r, c = 0, 0
    while True:
        c+=slope[0]
        r+=slope[1]
        if r>=len(paths):
            break
        else:
            if paths[r][c % len(paths[r])] == "#":
                trees+=1
    
    total_trees *= trees

print(total_trees)

