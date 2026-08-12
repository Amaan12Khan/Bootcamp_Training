def recursion(n):
    if n==0:
        return
    print(n)
    recursion(n-1)
    print(n)
n=int(input("Enter a number: "))
recursion(n)