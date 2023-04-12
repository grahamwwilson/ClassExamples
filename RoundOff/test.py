#
# Demonstrate round-off issues with 64-bit floating point numbers
#
h=1.0
one=1.0
for i in range(100):
    x = one + h
    print('Loop index',i,' h:',h,' x=1+h:',x,' x-1: ',x-one)
    h = h/2.0   
