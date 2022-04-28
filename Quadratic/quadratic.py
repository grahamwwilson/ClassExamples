# Solve quadratic equation three separate ways

from quadraticMethods import *
       
a = 1.0e-15
b = 6.76e-4
c = -6.76e-4

#a = 2.5
#b = 3.0
#c = 1.0

x1, x2 = HighSchool(a,b,c)
#print('High School:','x1 = ',x1,'x2 = ',x2)
# instead use python formatting 
print('{:16s} {:3s} {:.16e} {:3s} {:.16e}'.format('High School:','x1:',x1,'x2:',x2))

x1, x2 = Fagnano(a,b,c)
print('{:16s} {:3s} {:.16e} {:3s} {:.16e}'.format('Fagnano:','x1:',x1,'x2:',x2))

x1, x2 = Numerical(a,b,c)
print('{:16s} {:3s} {:.16e} {:3s} {:.16e}'.format('Numerical:','x1:',x1,'x2:',x2)) 

