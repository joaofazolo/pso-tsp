import math
import numpy
from swarm import Swarm
from particle import Particle
import random
from sys import argv

def pso(matrix,nParticles,ac1,ac2,nIter,nStuck):
    swarm = Swarm(nParticles,ac1,ac2)
    swarm.randomPosition(matrix)
    count = 0
    for i in range(0,nIter):
        if(count == nStuck):
            break
        # print "Iteration " + str(i+1)
        oldFitness = swarm.bestFitness
        swarm.evaluateFitness(matrix)
        swarm.updateBests()
        swarm.updateSpeeds()
        swarm.updatePositions()
        newFitness = swarm.bestFitness
        if(oldFitness == newFitness):
            count = count+1
        else:
            count = 0
        # print
    return (swarm.bestPosition, round(swarm.bestFitness,2))

    
#Calcula custo de uma permutacao
def func_obj(matriz,permutacao):
    custo = 0
    for i in range(0,len(permutacao)-1):
        j = i+1
        custo = custo + matriz[permutacao[i]-1][permutacao[j]-1]

    custo = custo + matriz[permutacao[-1]-1][permutacao[0]-1]

    return custo

