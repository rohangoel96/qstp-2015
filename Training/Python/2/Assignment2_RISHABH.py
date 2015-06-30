day = int(raw_input("Enter Date : "))
month = int(raw_input("Enter Month : "))
year = int(raw_input("Enter Year : "))
print "%d/%d/%d" %(day, month, year)

month_increment = int(raw_input("How many months to move ahead : "))
month = month_increment + month
if month > 12 :
    month %= 12
    year += 1

print "%d/%d/%d" %(day, month, year)
