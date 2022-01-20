import argparse

parser = argparse.ArgumentParser(description='Pendulum Timer Simulator with ODE')
parser.add_argument("-n", "--noscs", type=int, default=130, help="Number of oscillations to simulate")
parser.add_argument("-d", "--drag", type=float, default=0.032, help="Drag")

args=parser.parse_args()
print('Found argument list: ')
print(args)
NOSCS = args.noscs      # Number of oscillations to simulate       
drag=args.drag          # Drag angular acceleration at equilibrium position [rad/s^2] 
