# UniformArgParse.py
# Illustrate standard uniform random number generator
# Here we add argument parsing
import random
import argparse  

parser = argparse.ArgumentParser(description='Uniform random number demonstration')
parser.add_argument("-n", "--ngen", type=int, default=10, help="Number of random numbers to generate")
parser.add_argument("-s", "--seed", type=int, default=203, help="Random number seed")

args=parser.parse_args()
print('Found argument list: ',args)

NGEN = args.ngen
SEED = args.seed

# Initialize the random number generator using specified seed
random.seed(SEED)

print('NGEN set to',NGEN)
print('SEED set to',SEED)

# Generate uniform random numbers
for i in range(NGEN):
    u = random.random() # standard uniform random numbers 
                        # in range [0.0,1.0)
    print('uniform random number',i,'u =',u)
