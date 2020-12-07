
#FIRST HALF

def search_bag(bags, current_bags, already_counted=[], count=0):
    if len(current_bags) == 0:
        return count
    else:
        next_bags = []
        for out_bag in current_bags:
            for in_bag in bags:
                if out_bag in in_bag[1]:
                    nextbag = in_bag[0].split(" bags")[0]
                    if nextbag not in already_counted:
                        next_bags.append(nextbag)
                        already_counted.append(nextbag)
                        count+=1

        return search_bag(bags, next_bags, already_counted, count)

with open("input.txt", "r") as f:
    f = f.readlines()
    f = [line.strip(".\n").split(" contain ") for line in f]

print(search_bag(f, ["shiny gold",]))


