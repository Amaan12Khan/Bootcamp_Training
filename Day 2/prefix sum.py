nums=[1,2,3,4]
runningSum=[]
sums=0
for i in nums:
    sums+=i
    runningSum.append(sums)
print(runningSum)