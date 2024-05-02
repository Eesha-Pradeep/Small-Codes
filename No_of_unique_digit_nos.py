s = 0
for i in range(100,1000):
  for j in str(i):
    if str(i).count(j)!=1:
      break
  else:
    print(i, end=" ")
    s+=1
print()
print(f"There are {s} numbers between 100 and 999!")