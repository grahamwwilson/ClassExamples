import math
import argparse

def f(x):
    f = x**2*(math.cos(x))**4
    return f

def main(N,a,b):

    Iexact = math.pi* ( (math.pi)**2 + (17.0/32.0))
    print(Iexact)

    a = 0.0
    b = 2.0*math.pi

# Implement Boole's rule. Based on an extended version of the 5-point closed formula.
    dx = (b-a)/(4.0*N)
    Isum = 0.0
    for i in range(4*N+1):
        xi = a + i*dx
        if i==0 or i==4*N:
            Isum += 14.0*f(xi)
        elif i%2==1:
            Isum += 64.0*f(xi)
        elif i%4==2:
            Isum += 24.0*f(xi)
        else:
            Isum += 28.0*f(xi)
            
    Isum = Isum*dx/45.0    

    print("Boole's method",'with N =',N,', 4*N = ',4*N) 
    print('Isum                 = ',Isum)
    print('Iexact               = ',Iexact)
    print('Deviation            = ',Isum-Iexact)
    print('fractional deviation = ',(Isum-Iexact)/Iexact)
    
    return Isum

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Integral using midpoint method')
    parser.add_argument("-n", "--nstrips", type=int, default=100, help="Number of strips")
    parser.add_argument("-a", "--xmin", type=float, default=0.0, help="xmin")
    parser.add_argument("-b", "--xmax", type=float, default=2.0*math.pi, help="xmax")    
        
    args=parser.parse_args()
    print('Found argument list: ',args)
    
    I1 = main(args.nstrips//2,args.xmin, args.xmax)
    I2 = main(args.nstrips, args.xmin, args.xmax)
    
    print('I1 = ',I1)
    print('I2 = ',I2)
    print('empirical error bound ',abs(I2-I1))
    print('probable error        ',abs(I2-I1)/63.0)
    Ibetter = I2 + (I2-I1)/63.0
    print('Ibetter = ',Ibetter)
    Iexact =  math.pi* ( (math.pi)**2 + (17.0/32.0))
    print('Ibetter deviation = ',Ibetter-Iexact)
    print('Ibetter fractional deviation = ',(Ibetter-Iexact)/Iexact)
    
    
