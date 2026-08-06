s='abc123xyz456'
digits = ''
for i in s:
    if i.isdigit():
        digits += i
print(digits)