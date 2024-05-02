no = input("Enter number: ")
import string
invalid = list(string.ascii_letters+string.punctuation)
for i in [".", "E", "e", "+", "-"]:
  invalid.remove(i)
for i in invalid:
  if i in no:
    a = False
    break
else:
  a = True
for i in list(string.digits):
  if str(i) in no:
    break
else:
  a = False
if not a:
  print(False)
  exit()
for k in ["E", "e"]:
    if k in no:
      Esplit = no.partition(k)
      if no[0]==k:
        print(False)
        exit()
      elif "." in Esplit[2]:
        print(False)
        exit()
      elif not Esplit[2]:
        print(False)
        exit()    
if len(no)>1 and (no[1]=="+" or no[1]=="-"):
  print(False)
  exit()
else:
  for i in ["e", "E", "."]:
    if i in no and no.count(i)>1:
      print(False)
      break
  else:
    print(True)