# nums = [1,0,1,1,0,1]
nums = [1,1,0,1,1,1]

def func(nums):
    count=0
    maxCount=0
    for i in nums:
        if i == 1:
            count += 1
        else:
            if maxCount < count:
                maxCount = count
                count=0
    if  maxCount < count:
        maxCount = count
        count=0
    
    print(maxCount)

func(nums)