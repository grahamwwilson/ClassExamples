# quadsArgs.py
from argparse import ArgumentParser
import math

# See https://stackoverflow.com/questions/26785952/python-argparse-as-a-function

def getArgs(argv=None):
# Set command line configurable parameters. Do python3 program.py -h to see this in action.
    parser = ArgumentParser(description="Numerical integration by Simpson's method")
    parser.add_argument("-n", "--n", type=int, default=100, help="Half-number of strips (N)")
    parser.add_argument("-a", "--a", type=float, default=0.0, help="Lower limit of integration")
    parser.add_argument("-b", "--b", type=float, default=2.0*math.pi, help="Upper limit of integration")
         
    args=parser.parse_args(argv)
    print('(quadsArgs.getArgs     ) Found argument list: ',args)
    
    return args
    
def showArgs(N,a,b):
# Check these are what we want
    print('(quadsArgs.ShowArgs    ) Program has set')
    print('N:   ',N)
    print('a:   ',a)
    print('b:   ',b)
    return
        
def getArguments(argv=None):
# Do 2 things at once.
# i)   set defaults and parse them using getArgs above
# ii)  set values for our program

    args = getArgs(argv)

    print('(quadsArgs.getArguments) Assigning arguments to program variables')
    
    N = args.n
    a = args.a
    b = args.b
    return N,a,b    
