import sys

import site

stringoutput = ''
for i in range(1,sys.argv.__len__()):
    input = sys.argv[sys.argv.__len__()-i]
    inputlength = int(input.__len__())
    outputstring = ''



    for i in range(0,int(inputlength)):
        temp = input[int(inputlength-i-1)]
        outputstring = outputstring+temp 
    stringoutput=stringoutput+outputstring + ' '
print stringoutput
#    print outputstring
