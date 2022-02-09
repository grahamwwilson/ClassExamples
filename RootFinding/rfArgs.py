# rfArgs.py
from argparse import ArgumentParser

# See https://stackoverflow.com/questions/26785952/python-argparse-as-a-function

def getArgs(argv=None):
# Set command line configurable parameters. Do python3 program.py -h to see this in action.
    parser = ArgumentParser(description="Root finding")
    parser.add_argument("-a", "--a", type=float, default=2.5, help="Bracketing xmin value")
    parser.add_argument("-b", "--b", type=float, default=3.5, help="Bracketing xmax value")
    parser.add_argument("-t", "--tol", type=float, default=1.0e-15, help="Tolerance on x")         
         
    args=parser.parse_args(argv)
    print('(rfArgs.getArgs     ) Found argument list: ',args)
    
    return args
    
def showArgs(a,b,tol):
# Check these are what we want
    print('(rfArgs.ShowArgs    ) Program has set')
    print('a:   ',a)
    print('b:   ',b)
    print('tol: ',tol)
    return
        
def getArguments(argv=None):
# Do 2 things at once.
# i)   set defaults and parse them using getArgs above
# ii)  set values for our program

    args = getArgs(argv)

    print('(rfArgs.getArguments) Assigning arguments to program variables')
    
    a = args.a
    b = args.b
    tol = args.tol
   
    return a,b,tol    
