import copy

with open("input.txt", "r") as f:
    f = f.readlines()
    f = [[line.strip("\n").split()[0], int(line.strip("\n").split()[1])] for line in f]

#FIRST HALF

def run_through(ls):
    i=0
    acc_count = 0
    visited = []
    final=False
    while True:
        if i>=len(ls):
            final=True
            break

        instruc, offset = ls[i]
        
        visited.append(i)

        if instruc == "nop":
            i+=1
        elif instruc == "acc":
            acc_count+=offset
            i+=1
        else:
            i+=offset

        if i in visited:
            break

    return (acc_count, visited, final)

acc_count, visited, _ = run_through(f)
print(acc_count)

#SECOND HALF

visited = [i for i in visited if f[i][0] in ("jmp", "nop")]
for x in visited:
    f2=copy.deepcopy(f)

    if f2[x][0] == "jmp":
        f2[x][0] = "nop"

    elif f2[x][0] == "nop":
        f2[x][0] = "jmp"

    acc_count, _, final = run_through(f2)
    if final:
        print(acc_count)
        break