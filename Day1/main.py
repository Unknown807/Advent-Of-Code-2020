
with open("input.txt", "r") as nums:
    nums = nums.readlines()
    nums = [line.strip("\n") for line in nums]

#FIRST HALF

def first(nums):
    for i in range(len(nums)):
        inum=nums[i]
        for j in range(len(nums)):
            jnum=nums[j]
            if len(str(inum)) == 4 and len(jnum) == 4:
                continue
            
            jnum=int(jnum)
            inum=int(inum)

            if inum+jnum == 2020:
                print(inum*jnum)
                return

#SECOND HALF

def second(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if int(nums[i])+int(nums[j])+int(nums[k]) == 2020:
                    print(int(nums[i])*int(nums[j])*int(nums[k]))
                    return

first(nums)
second(nums)