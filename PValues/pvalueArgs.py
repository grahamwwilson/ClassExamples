# pvalueArgs.py
from argparse import ArgumentParser

# See https://stackoverflow.com/questions/26785952/python-argparse-as-a-function

def getArgs(argv=None):
# Set command line configurable parameters. Do python3 program.py -h to see this in action.
    parser = ArgumentParser(description="Calculate p-value (upper tail probability) for Chi-Squared distribution")
    parser.add_argument("-w", "--which", type=int, default=0, help="Chi-squared (0) or reduced chisq (1)")
    parser.add_argument("-v", "--value", type=float, default=4.0, help="Value")
    parser.add_argument("-n", "--ndof", type=int, default=1, help="Number of degrees of freedom")   
         
    args=parser.parse_args(argv)
    print('(pvalueArgs.getArgs     ) Found argument list: ',args)
    
    return args
    
def showArgs(which, value, ndof):
# Check these are what we want
    print('(pvalueArgs.ShowArgs    ) Program has set')
    print('which:   ',which)
    print('value:   ',value)
    print('ndof:   ',ndof)
    return
        
def getArguments(argv=None):
# Do 2 things at once.
# i)   set defaults and parse them using getArgs above
# ii)  set values for our program

    args = getArgs(argv)

    print('(pvalueArgs.getArguments) Assigning arguments to program variables')
    
    which = args.which
    value = args.value
    ndof = args.ndof
   
    return which,value,ndof    
