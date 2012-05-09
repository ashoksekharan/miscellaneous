#numbers for circle in a program
#Numbers of 39*4 - 22*7 = 2 and 5 to 15 mapping for angles therefore 1.23, 4 points for stability of circle and output is 1 circle.
#1.23 2 4 1 First 2 points then 4 then 1
# convert by 10 to 12 20 40 10
# Transitions are 6 1.23*5 2=2 and 4/2 and 0 congruency theorem such as rhombus

# We are changing transitions of first and last numbers to get circle instead of ellipse
import sys

letter = sys.argv[1]
radius = sys.argv[2]

y = ''
for i in  range(0,14):
    if (i==11):
        y = y + letter 
    y = y + ' ' 
print y, letter 

y = ''
for i in  range(0,18):
    if (i==8):
        y = y + letter 
    y = y + ' '
print y, letter 

y = ''
for i in  range(0,20):
    if (i==6):
        y = y + letter 
    y = y + ' ' 
print y, letter

y = ''
for i in  range(0,20):
    if (i==6):
        y = y + letter 
    y = y + ' ' 
print y , letter

y = ''
for i in  range(0,18):
    if (i==8):
        y = y + letter 
    y = y + ' '
print y , letter

y=''
for i in  range(0,14):
    if (i==11):
        y = y + letter 
    y = y + ' ' 
print y, letter 
