import sys

alphabet = sys.argv[1]
lines = int(sys.argv[2])
print "Element to be printed is", alphabet
print "Repetition upto", lines, "lines"

for k in range(0,lines):
    y = ''
    tmp = int(2**(k))
    tmp1 = int(2**(lines))
    if (tmp1>150):
        print "Out Of Range"
        exit()
    tmp2 = int(75-(2**k/2))
    for i in range(0,tmp2):
         y = y + ' ' 
    for i in range(0,tmp):
         y = y + alphabet 
    print y
