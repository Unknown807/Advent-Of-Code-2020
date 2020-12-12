with open("input.txt", "r") as f:
    f = f.readlines()
    f = [line.strip("\n") for line in f]

#FIRST HALF

direc = "E"
vals = {"N":[0, ["E","S","W"]], 
        "S":[0, ["W", "N", "E"]],
        "E":[0, ["S", "W", "N"]], 
        "W":[0, ["N", "E", "S"]]}

for line in f:
    new_direc = line[0]
    val = int(line[1:])

    if new_direc == "F":
        vals[direc][0] += val
    elif new_direc == "R":
        direc = vals[direc][1][(val//90)-1]
    elif new_direc == "L":
        direc = vals[direc][1][((360-val)//90)-1]
    else:
        vals[new_direc][0] += val
        
ns = abs(vals["N"][0]-vals["S"][0])
ew = abs(vals["E"][0]-vals["W"][0])

print(ns+ew)