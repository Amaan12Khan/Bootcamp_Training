nums=int(input("enter a number:"))
arr=[10,7,3,12,15]
floor=-1
ceil=-1
for i in arr:
    if i<=nums:
        if floor==-1 or i>floor:
            floor=i
    if i>=nums:
        if ceil==-1 or i<ceil:
            ceil=i
print("floor value of the number is: ",floor)
print("ceil value of the number is: ",ceil)