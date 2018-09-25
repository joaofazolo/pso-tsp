from pso import pso
from tsp_reader import tsp_reader
from brute_force import brute_force
from sys import argv

NPARTICLES = 10
ACCELERATION1 = 0.4
ACCELERATION2 = 0.2
NITERATIONS = 100

try:
    matrix = tsp_reader()
    print pso(matrix,NPARTICLES,ACCELERATION1,ACCELERATION2,NITERATIONS)
    print brute_force([1],matrix,[2,3,4,5,6,7,8,9])
    
except Exception as exc:
    print exc.message
