arr = eval(input("Enter an array of integers: "))
final_arr = []
while arr:
  amin = min(arr)
  a = arr.pop(arr.index(amin))
  bmin = min(arr)
  b = arr.pop(arr.index(bmin))
  final_arr.extend([b,a])
print(final_arr)