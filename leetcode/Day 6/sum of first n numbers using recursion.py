def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)
n = int(input("Enter a number: "))
print("the sum of first", n, "numbers is:", sum(n))