with open("input.txt", "r") as f:
    f = f.readlines()
    f = [int(line.strip("\n")) for line in f]

#FIRST HALF

def sum_nums(num, prev_nums):
    not_valid = True
    for i in prev_nums:
        for j in prev_nums:
            if i+j == num:
                not_valid=False
                break
    
    return not_valid

prev_nums = f[:25]

for num in f[25:]:
    if sum_nums(num, prev_nums):
        print(num)
        break
    
    prev_nums.append(num)
    prev_nums=prev_nums[1:26]
    
#SECOND HALF

def find_weakness(f):
    def sum_cont_nums(nums, num_to_match):
        if len(nums) > 1:
            if sum(nums) == num_to_match:
                print(max(nums)+min(nums))
                return True
        return False

    invalid_num = 400480901
    prev_nums = f[:f.index(invalid_num)]

    for rng in range(2, f.index(invalid_num)):
        prev_nums = f[:rng]
        for num in f[rng:]:
            for i in range(rng):
                way1=prev_nums[i:]
                way2=prev_nums[:i+1]
                    
                if sum_cont_nums(way1, invalid_num):
                    return

                if sum_cont_nums(way2, invalid_num):
                    return
            
            prev_nums.append(num)
            prev_nums=prev_nums[1:rng+1]

find_weakness(f)
    

