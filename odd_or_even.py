#Mechanical model of the fillet counter is based on infinite counting numbers using compression and expansion. use a mechanical model first
# Balloon squeezable bottle and hammer.

import sys

#take input as number of elements that are to be completely procured as a procedure.

number = float(sys.argv[1])
print "Number to be checked is", sys.argv[1], number

# Purpose of this algorithm is to convert x space y time to y space x time. let its name be fillet counter. Let model of expansion be sin(theta) and compression be cosine(theta). This is called as an impulse to come up with sufficient back up for a saw tooth waveform that we created in papers.pdf, for example.

if (number%2) == 1:
    print "Number is Odd"

if (number%2) == 0:
    print "Number is Even"

