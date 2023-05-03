nums = [int(item) for item in input().split(",")]
outnum = []

for i in nums:
    for j in range(i,len(nums)):
        for k in range(j,len(nums)):
            if (nums[i]+nums[j]+nums[k] == 0):
                if (i != j and i != k and j != k):
                    a=[nums[i],nums[j],nums[k]]
                    a.sort()
                    outnum.append(a) 
            else:
                outnum += []
result = [] 
for i in outnum: 
    if i not in result: 
        result.append(i) 
print(result)
