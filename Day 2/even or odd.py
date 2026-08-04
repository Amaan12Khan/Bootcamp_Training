arr=[1,2,3,4,5,6,7,8,9,10]
odd_count=0
even_count=0
for i in arr:
    if i % 2 ==0:
        even_count+=1
    else:
        odd_count+=1
print("even no. in array",even_count)
print("odd no. in array",odd_count)
