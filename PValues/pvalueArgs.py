# pvalueArgs.py
from argparse import ArgumentParser

# See https://stackoverflow.com/questions/26785952/python-argparse-as-a-function

def getArgs(argv=None):
# Set command line configurable parameters. Do python3 program.py -h to see this in action.
    parser = ArgumentParser(description="Calculate p-value (upper tail probability) for Chi-Squared distribution")
    parser.add_argument("-c", "--chsq", type=float, default=6.0, help="Chi-squared value")
    parser.add_argument("-n", "--ndof", type=int, default=2, help="Number of degrees of freedom")   
         
    args=parser.parse_args(argv)
    print('(pvalueArgs.getArgs     ) Found argument list: ',args)
    
    return args
    
def showArgs(chsq,ndof):
# Check these are what we want
    print('(pvalueArgs.ShowArgs    ) Program has set')
    print('chsq:   ',chsq)
    print('ndof:   ',ndof)
    return
        
def getArguments(argv=None):
# Do 2 things at once.
# i)   set defaults and parse them using getArgs above
# ii)  set values for our program

    args = getArgs(argv)

    print('(pvalueArgs.getArguments) Assigning arguments to program variables')
    
    chsq = args.chsq
    ndof = args.ndof
   
    return chsq,ndof    
