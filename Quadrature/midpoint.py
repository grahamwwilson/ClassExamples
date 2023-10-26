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

# Implement N Riemann sums evaluated at mid-point of each strip.
    dx = (b-a)/N
    Isum = 0.0
    for i in range(N):
        xi = a + dx*i + 0.5*dx
        print(i, xi, xi/b, f(xi))
        Isum += f(xi)
    Isum = Isum*dx    

    print('middle Riemann sum method') 
    print('Isum                 = ',Isum)
    print('Iexact               = ',Iexact)
    print('Deviation            = ',Isum-Iexact)
    print('fractional deviation = ',(Isum-Iexact)/Iexact)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Integral using midpoint method')
    parser.add_argument("-n", "--nstrips", type=int, default=100, help="Number of strips")
    parser.add_argument("-a", "--xmin", type=float, default=0.0, help="xmin")
    parser.add_argument("-b", "--xmax", type=float, default=2.0*math.pi, help="xmax")    
        
    args=parser.parse_args()
    print('Found argument list: ',args)
    
    main(args.nstrips, args.xmin, args.xmax)
