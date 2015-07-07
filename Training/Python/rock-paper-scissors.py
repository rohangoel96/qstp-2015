# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import random
"""Rock - 0,Paper - 1,Scissor - 2"""
def name_to_number(choice):
    if choice == "Rock":
        num = 0
    elif choice == "Paper":
        num = 1
    else:
        num = 2
    return num
def number_to_name(num1):
    if num1 == 0:
        return "Rock"
    elif num1 == 1:
        return "Paper"
    else:
        return "Scissor"
def decision_making(a,b):
    if a == b:
        return "Please select a different choice"
    elif a - b < 0:
        if (a-b) % 3 <= 1:
            return a
        else:
            return b
    elif a - b > 0:
        if (a-b) <= 1:
            return a
        else:
            return b
    else:
        return "Error"
    
player_choice = raw_input("Enter a choice: ")
computer_choice = random.randint(0,2)
print "Player has chosen %s " % player_choice
print "Computer has chosen %s"% (number_to_name(computer_choice))
num2 = name_to_number(player_choice)
num3 = computer_choice

num_fin = decision_making(num2,num3)
if num_fin == num2:
    print "Player wins"
else:
    print "Computer wins"
  
    

