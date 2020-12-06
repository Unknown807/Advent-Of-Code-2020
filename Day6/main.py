with open("input.txt", "r") as f:
    f = f.read().split("\n\n")
    f = [ group.split("\n") for group in f]

# FIRST HALF

_sum=0
for group in f:
    counted = []
    count = 0
    for line in group:
        questions = [q for q in line if q not in counted]
        count+=len(questions)
        counted.extend(questions)
    _sum+=count

print(_sum)

# SECOND HALF

_sum=0
for group in f:
    questions = {}
    for line in group:
        [ questions.update({x:questions.get(x, 0)+1}) for x in line ]
    count = sum([1 for v in questions.values() if v==len(group)])
    _sum+=count
    
print(_sum)
