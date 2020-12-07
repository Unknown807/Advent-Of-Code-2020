with open("input.txt", "r") as passwords:
    passwords = passwords.readlines()
    passwords = [line.strip("\n") for line in passwords]

passwords = [password.split(":") for password in passwords]
for i in range(len(passwords)):
    ranges, letter = passwords[i][0].split(" ")
    range_1, range_2 = ranges.split("-")
    word = passwords[i][1].strip(" ")
    passwords[i] = [int(range_1), int(range_2), letter, word]

#FIRST HALF

valid=0
for i in passwords:
    if i[0] <= i[3].count(i[2]) <= i[1]:
        valid+=1

print(valid)

#SECOND HALF

valid=0
for i in passwords:
    #if i[0] <= i[3].count(i[2]) <= i[1]:
        #valid+=1
    limit=0
    if i[3][i[0]-1] == i[2]:
        limit+=1
    if i[3][i[1]-1] == i[2]:
        limit+=1
    if limit == 1:
        valid+=1

print(valid)