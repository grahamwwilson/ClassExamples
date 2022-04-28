# Solve quadratic equation three separate ways

from quadraticMethods import * 
       
a = 1.0e-15
b = 6.76e-4
c = -6.76e-4

x1, x2 = HighSchool(a,b,c)
print('High School:','x1 = ',x1,'x2 = ',x2)

x1, x2 = Fagnano(a,b,c)
print('Fagnano:    ','x1 = ',x1,'x2 = ',x2)

x1, x2 = Numerical(a,b,c)
print('Numerical:  ','x1 = ',x1,'x2 = ',x2)
