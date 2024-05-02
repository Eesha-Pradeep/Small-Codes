import itertools 

nos = eval(input("Enter the list of integers: "))
no = int(input("Enter final sum of numbers in subsets: "))
subsets = []
for i in range(len(nos)+1):
    subsets.extend(list(itertools.combinations(nos, i)))
    
for i in subsets:
    if sum(i)==no:
        print(i)

