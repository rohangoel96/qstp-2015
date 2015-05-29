date = raw_input("Enter a date:")
month = raw_input("Enter a month:")
year = raw_input("Enter a year:")
print date + "/" + month + "/" + year
move_ahead = raw_input("No. of months to move ahead")
if int(month) + int(move_ahead) > 12:
   year = int(year) + 1
   month = int(month) + int(move_ahead) - 12
else:
   month = int(month) + int(move_ahead)
print date + "/" + str(month) + "/" + str(year)
