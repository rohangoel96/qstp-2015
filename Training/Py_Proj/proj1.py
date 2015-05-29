date = input("Enter date:")
month = input("Enter month:")
ahead = input("How many months to move ahead:")

if month+ahead > 12:
	month = month + ahead - 12
else:
	month = month + ahead

print(str(date) + "/" + str(month))
