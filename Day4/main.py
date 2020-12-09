with open("input.txt", "r") as f:
    f = f.read().split("\n\n")
    f = [line.replace("\n", " ") for line in f]
    f =  [line.split() for line in f]
    
    passports = []

    for group in f:
        newgroup = {}
        for field in group:
            k,v = field.split(":")
            newgroup.update({k:v})
        passports.append(newgroup)


#FIRST HALF

valid=0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for group in passports:
    checks=0
    for field in fields:
        if field in group.keys():
            checks+=1
    if checks == 7:
        valid+=1

print(valid)

#SECOND HALF

valid=0
for group in passports:
    checks=0
    for field in group.keys():
    
        if field == "byr":
            if 1920 <= int(group[field]) <= 2002: checks+=1

        if field == "iyr":
            if 2010 <= int(group[field]) <= 2020: checks+=1

        if field == "eyr":
            if 2020 <= int(group[field]) <= 2030: checks+=1

        if field == "hgt":
            measure = group[field][-2:]
            val = group[field][:-2]
            if measure == "cm":
                if 150 <= int(val) <= 193: checks+=1
            elif measure == "in":
                if 59 <= int(val) <= 76: checks+=1
        
        if field == "hcl":
            val = group[field]
            if val[0] == "#" and len(val[1:]) == 6 and val[1:].isalnum(): checks+=1

        if field == "ecl":
            if group[field] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"): checks+=1

        if field == "pid":
            val = group[field]
            if len(val) == 9 and val.isdigit(): checks+=1

    if checks == 7:
        valid+=1

print(valid)