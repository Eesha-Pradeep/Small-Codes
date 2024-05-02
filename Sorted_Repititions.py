l1 = eval(input("Enter a list: "))
b = []
for i in l1:
    s = 0
    if i in b:
        l1.remove(i)
    c = l1.count(i)
    if c>1 and i not in b:
       b.append(i)
b.sort()
if len(b)!=0:
    print(b)
else:
    print(-1)