from particle import Particle
from random import shuffle

#Classe swarm
class Swarm:
    bestPosition = []
    bestFitness = 9999999999999999999
    particles = []

    def __init__(self,nParticles,acceleration1,acceleration2):
        self.acceleration1 = acceleration1
        self.acceleration2 = acceleration2
        for i in range(nParticles):
            p = Particle(i)
            self.particles.append(p)
    
    #Atualizada velocidade das particulas
    def updateSpeeds(self):
        for particle in self.particles:
            particle.updateSpeed(self.acceleration1,self.acceleration2,self.bestPosition)

    #Retorna uma particula pelo id
    def getParticle(self,id):
        return self.particles[id]

    def updatePositions(self):
        for particle in self.particles:
            particle.updatePosition()

    def evaluateFitness(self,matrix):
        for particle in self.particles:
            particle.evaluateFitness(matrix)

    def updateBests(self):
        bestfitness = self.bestFitness
        bestposition = self.bestPosition
        for particle in self.particles:
            particle.updateBest()
            if(particle.getBestFitness() < bestfitness):
                bestposition = particle.getBestPosition()
                bestfitness = particle.getBestFitness()
        # print "Global best fitness updated from " + str(self.bestFitness) + " to " + str(bestfitness)
        # print "Global best position updated from " + str(self.bestPosition) + " to " + str(bestposition)
        self.bestPosition = bestposition
        self.bestFitness = bestfitness

    def randomPosition(self,matrix):
        for particle in self.particles:
            init = [i+1 for i in range(len(matrix))]
            shuffle(init)
            particle.setPosition(init)
            # print "Particle "+str(particle.id)+" starting at "+str(particle.position)
            particle.bestPosition = init
    