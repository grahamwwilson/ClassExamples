from multiprocessing import Process
import os

def print_func(continent):
# dummy loop so that this takes a finite amount of time
    N = 500000000
    for i in range(N):
        j = i
    print('The continent name is : ', continent,' (based on pid ',os.getpid(),')')

def myprogram():
    names = ['1: Asia ', '2: North America', '3: South America', '4: Europe', '5: Africa', '6: Oceania']
    procs = []

    # instantiating process with arguments
    for name in names:
        print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()
        
    # Let's check what processes we have
    print('Processes: ',procs)

    # Need to tell each process to complete
    for proc in procs:
        proc.join()
        
    print('All processes completed')  

if __name__ == "__main__":  # confirms that the code is under main function
    myprogram()
