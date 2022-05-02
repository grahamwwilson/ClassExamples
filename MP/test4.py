from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print(' ')

def f(name):
    info('function f')
    print('Hello', name)

if __name__ == '__main__':

    info('main')
    
    p = Process(target=f, args=('Bob',))
    p.start()
    p.join()
