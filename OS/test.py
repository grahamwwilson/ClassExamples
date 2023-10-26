import os
import random
import argparse

def main(seed, nrep):
    " Run p-value calculator multiple times "
    random.seed(seed)

    i = 0
    while i < nrep:
        z = random.gauss(0.0, 1.0)
        outfile = "out" + str(i) + ".out"
        command = "python3 ../PValues/pvalue.py -c "+str(z**2)+" -n 1 > "+str(outfile)
        print("Running command for i = ",i)
        os.system(command)
        i += 1
        
    os.system("grep -h \"p-value\" out*.out | sort -g -k5")    
    
if __name__ == '__main__':
    # execute only if run as a script / from the command line
    print('Executing test.py main conditional statements')  # Add print for clarity on execution mode
        
    parser = argparse.ArgumentParser(description='Run p-value calculator multiple times')       
    parser.add_argument("-s", "--seed", type=int, default=1234,   help="Random number seed (default: 1234)")
    parser.add_argument("-n", "--nrep", type=int, default=10,   help="Number of repetitions (default: 10)")
    
    args=parser.parse_args()
    print('Found argument list: ',args)
    main(args.seed, args.nrep)
