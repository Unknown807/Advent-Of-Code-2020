with open("input.txt", "r") as f:
    f = f.readlines()
    f = [int(line.strip("\n")) for line in f]

#FIRST HALF

source_volt = 0
device_volt=max(f)+3

one_diffs=0
three_diffs=1

f=sorted(f)
for num in f:
    if num-source_volt == 1:
        one_diffs+=1
    elif num-source_volt == 3:
        three_diffs +=1
    
    source_volt=num

print(one_diffs*three_diffs)

#SECOND HALF - WORKS FOR ALL BUT THE LONGEST OF INPUTS

def num_diff(num, source_volt):
    if 1 <= num-source_volt <= 3:
        return num
    else:
        return None

def run_through_nums(paths, num):
    if paths.get(num, None) is None:
        return 1
    else:
        total = 0
        for adapter in paths.get(num):
            total+=run_through_nums(paths, adapter)
        
        return total
        
source_volt = 0
f=sorted(f)
total=0

paths = {}

for adapter in f:
    next_num = [num for num in f if num_diff(num, source_volt) != None]
    paths.update({source_volt:next_num})
    source_volt=adapter

#print(run_through_nums(paths, 0))

#SECOND HALF FASTER (LOOKED UP)

f+=[0, max(f)+3]
f=sorted(f)

limit=max(f)+1

paths = [0]*limit
paths[0] = 1

for i in range(1, limit):
    for x in range(1, 4):
        _sum=i-x
        if (_sum) in f:
            paths[i] += paths[_sum]

print(paths[-1])
