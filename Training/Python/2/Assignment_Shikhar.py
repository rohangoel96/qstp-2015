print "Enter date"
d=int(input())
print "Enter month"
m=int(input())
print d,"/",m
print "How many months to move ahead"
n=(int(input())+m)%12
print d,"/",n
