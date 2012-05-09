import sys

import site

input = sys.argv[1]

inputlength = int(input.__len__())

for i in range(0,int(inputlength/2)):
    temp = int(inputlength-i)
    print input[temp-1]
    if (input[i] != input[temp-1]):
        print "Not a Palindrome"
        exit()

