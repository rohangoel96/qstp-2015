# -*- coding: utf-8 -*-
'''Problem 1.
Write a program that does the following in order:
1. Asks the user to enter the date
2. Asks the user to enter the month
3. Display the date in DD/MM format
4. Ask the user how many months to move ahead and display the date

An example of an interaction with your program is shown below (the words with a single star
are from the computer, based on your commands, the words with a dollar are a user’s input –

$Enter Date
**25
$Enter Month:
**02
$25/2
$How many months to move ahead:
**2
$25/4

(Yeah, that's my birthday. More self obsession- Anmol)

If it's too easy, try having a year field and wrapping around for more than 12 months. Completely optional this is.'''

date=int(raw_input("Enter Date : "))
month=int(raw_input("Enter Month : "))
print date,'/',month
move=int(raw_input("How many months to move ahead: "))
print date,'/',(month+move)%12
