dict={101:'ram',102:'shyam',103:'mohan'}
dict[104]='ramesh'
print(dict.get(101))
print(dict.get(105,0))
if 102 in dict:
    print("Key is present in the dictionary")
dict.pop(103)
print(len(dict))
print(dict.keys())
print(dict.values())
print(dict.items())
dict.clear()