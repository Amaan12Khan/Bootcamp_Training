s=input("enter a string:")
uppercase_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in s:
    if i in uppercase_string:
        s=s.replace(i,i.lower())
print(s)