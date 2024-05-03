dd = int(input("Enter the date in digits: "))
mm = input("Enter the month in its full form: ")
yy = int(input("Enter the year in its full form in digits: "))
leap = True
if yy%100==0:
  if yy%400!=0:
    leap = False
else:
  if yy%4!=0:
    leap = False
if mm.lower() not in ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]:
  print("Invalid date (month input incorrect)")
elif dd<1 or dd>31:
  print("Invalid date (date input incorrect)")
elif leap==False and mm.lower()=="february" and dd==29:
  print("Invalid date")
elif mm.lower()=="february" and dd>29:
  print("Invalid date (date/month input incorrect)")
elif mm.lower() in ["april", "june", "september", "november"] and dd>30:
  print("Invalid date (month/date input incorrect)")
else:
  print("The date is valid! :) ")