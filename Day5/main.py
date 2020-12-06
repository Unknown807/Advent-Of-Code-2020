with open("input.txt", "r") as f:
    f = f.readlines()
    f = [line.strip("\n") for line in f]

# FIRST HALF

 _max=0
 for letters in f:
     col_l, col_u = 0, 7
     row_l, row_u = 0, 127
     for letter in letters:
         if letter == "F":
             row_u = row_l+((row_u-row_l)//2)
         elif letter == "B":
             row_l = row_l+((row_u-row_l)/2+0.5)
         elif letter == "R":
             col_l = col_l+((col_u-col_l)/2+0.5)
         else: # L
             col_u = col_l+((col_u-col_l)//2)
     _sum = row_l * 8 + col_l
     if _sum > _max:
         _max=_sum
 print(_max)

# SECOND HALF

ids = []
for letters in f:
    col_l, col_u = 0, 7
    row_l, row_u = 0, 127
    for letter in letters:
        if letter == "F":
            row_u = row_l+((row_u-row_l)//2)
        elif letter == "B":
            row_l = row_l+((row_u-row_l)/2+0.5)
        elif letter == "R":
            col_l = col_l+((col_u-col_l)/2+0.5)
        else: # L
            col_u = col_l+((col_u-col_l)//2)
    _sum = row_l * 8 + col_l
    ids.append(_sum)

_id=0
for i in ids:
    if i+1 not in ids and i+2 in ids:
        _id = i+1

print(_id)
            
            
