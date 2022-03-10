# pendArgs.py
from argparse import ArgumentParser
import math

# See https://stackoverflow.com/questions/26785952/python-argparse-as-a-function

def getArgs(argv=None):
# Set command line configurable parameters. Do python3 program.py -h to see this in action.
    parser = ArgumentParser(description="Pendulum Motion")
    parser.add_argument("-a", "--a",  type=float, default=45.0, help="Initial launch angle (degrees)")
    parser.add_argument("-w", "--w",  type=float, default=0.0,  help="Initial angular velocity (rad/s)")    
    parser.add_argument("-g", "--g",  type=float, default=9.80, help="Acceleration due to gravity (m/s^2)")
    parser.add_argument("-l", "--l",  type=float, default=1.2,  help="Pendulum length (m)")    
    parser.add_argument("-d", "--dt", type=float, default=0.01, help="Time-step (s)")
    parser.add_argument("-s", "--s",  type=int,   default=2,    help="Stepper method (0=Euler, 2=RK2)")
    parser.add_argument("-t", "--t",  type=float, default=20.0, help="Evolution duration (s)")     
    parser.add_argument("-f", "--f",  type=str,   default="pendulum.dat", help="Output file name")           
       
    args=parser.parse_args(argv)
    print('(pendArgs.getArgs     ) Found argument list: ',args)
    
    return args
    
def showArgs(a, w, g, l, dt, s, t, f):
# Check these are what we want
    print('(pendArgs.ShowArgs    ) Program has set')
    print('a:   ',a, 'rad')
    print('w:   ',w, 'rad/s')
    print('g:   ',g, 'm/s^2')
    print('l:   ',l, 'm')    
    print('dt:  ',dt, 's')
    print('Stepper Method',s)
    print('tMax ',t,  's')
    print('Output file',f)    
    return
        
def getArguments(argv=None):
# Do 2 things at once.
# i)   set defaults and parse them using getArgs above
# ii)  set values for our program

    args = getArgs(argv)

    print('(pendArgs.getArguments) Assigning arguments to program variables')
    
    a = (math.pi/180.0)*args.a   # Convert to radians
    w = args.w
    g = args.g
    l = args.l
    dt = args.dt
    s = args.s
    t = args.t
    f = args.f
    return a, w, g, l, dt ,s, t, f 
