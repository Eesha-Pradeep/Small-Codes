n = input('''
Sample Run 1: (number in blue and bold is the user input)
Enter a positive number in the range [1000,9999]: ''')
c = 1
while len(n)!=4:
  print("Your number does not have 4 digits! Please try again.")
  c+=1
  print(f"Sample Run {c}: (number in blue and bold is the user input)")
  n = input('Enter a positive number in the range [1000,9999]: ')
print(f"The reverse of {n} is {n[::-1]}")