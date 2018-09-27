from pso import pso
from tsp_reader import tsp_reader
from brute_force import brute_force
from time import time
from sys import argv

#10-50
NPARTICLES = 30

#0.0 - 0.5
ACCELERATION1 = 0.4

#0.0 - 0.5
ACCELERATION2 = 0.4

#50-150
NITERATIONS = 150

#0-100
NSTUCKEDITERATIONS = 30

try:
    matrix = tsp_reader(argv[1])
    now = time()
    print (pso(matrix,NPARTICLES,ACCELERATION1,ACCELERATION2,NITERATIONS,NSTUCKEDITERATIONS)[1])
    then = time()
    timeSpent = then-now
    print (timeSpent)

    # print brute_force([1],matrix,[2,3,4,5,6,7,8,9,10])
    
except Exception as exc:
    print (exc.message)
