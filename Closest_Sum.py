l1 = eval(input("Enter the first list: "))
l2 = eval(input("Enter the second list: "))
x = int(input("Enter the desired number: "))
n1 = l1[0]
n2 = l2[0]
closest_sum = n1+n2
for i in range(len(l1)):
    for j in range(len(l2)):
        s = l1[i]+l2[j]
        if abs(closest_sum - x)>abs(s - x):
            closest_sum = s
            n1 = l1[i]
            n2 = l2[j]
print(f"The desired number was {x} but the closest sum was {closest_sum} of the numbers {n1} from the first list and {n2} from the second list.")