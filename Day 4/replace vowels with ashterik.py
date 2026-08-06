s='programming'
vowls='aeiouAEIOU'
for i in s:
    if i in vowls:
       s=s.replace(i,'*')
print(s)