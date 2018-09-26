from pso import pso
from tsp_reader import tsp_reader
from brute_force import brute_force
from sys import argv

NPARTICLES = 50
ACCELERATION1 = 1
ACCELERATION2 = 1
NITERATIONS = 200

try:
    matrix = tsp_reader()
    print pso(matrix,NPARTICLES,ACCELERATION1,ACCELERATION2,NITERATIONS)
    # print brute_force([1],matrix,[2,3,4,5,6,7,8,9,10])
    
except Exception as exc:
    print exc.message
