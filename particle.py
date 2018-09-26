import random

#Classe particula
class Particle:
    bestPosition = []
    bestFitness = 999999
    position = []
    fitness = 999999
    speed = []

    def __init__(self,id):
        self.id = id

    def getBestFitness(self):
        return self.bestFitness

    def getBestPosition(self):
        return self.bestPosition

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setPosition(self, newPosition):
        self.position = newPosition

#Avalia quao boa e a permutacao
    def evaluateFitness(self,matriz):
        permutacao = self.position
        custo = 0
        for i in range(0,len(permutacao)-1):
            j = i+1
            custo = custo + matriz[permutacao[i]-1][permutacao[j]-1]

        custo = custo + matriz[permutacao[-1]-1][permutacao[0]-1]
        self.fitness = custo
        # print "Evaluating fitness of particle " + str(self.id) + ": " + str(self.fitness)
    
    #Atualiza velocidade
    def updateSpeed(self,inertia,acceleration1,acceleration2,globalBest):
        # print "Updating speed of particle " + str(self.id)
        oldSpeed = self.speed

        newSpeed = []
        
        dice = random.random()
        r0 = random.random()/2
        r1 = random.random()/2
        r2 = random.random()/2
        newSpeed.extend(oldSpeed)

        #Componente local
        if(r1+acceleration1 >= dice):
            localComponent = self.diff(self.bestPosition)
            # print "Local component: " + str(localComponent)
            if(localComponent):
                newSpeed.extend(localComponent)

        #Componente global
        if(r1+acceleration1 >= dice):
            globalComponent = self.diff(globalBest)
            # print "Global component: " + str(globalComponent)
            if(globalComponent):
                newSpeed.extend(globalComponent)
        # print "New speed: " + str(newSpeed)
        self.speed = newSpeed
        # print "speed: " + str(self.speed)

    def updatePosition(self):
        for swap in self.speed:
            self.swap(swap)

    def getSpeed(self):
        return self.speed
    
    #Operacao para realizar o swap de duas cidades na permutacao (1,2)
    def swap(self,swap):
        aux = self.position[swap[0]]
        self.position[swap[0]] = self.position[swap[1]]
        self.position[swap[1]] = aux

    def diff(self,p):
        diff = []
        for i in range(len(p)):
            # print str(p[i]) + " , " + str(self.position[i])
            if(p[i] != self.position[i]):
                for j in range(len(self.position)):

                    if(p[i] == self.position[j]):
                        if([j,i] not in diff):
                            diff.append([i,j])
        return diff
                
    def updateBest(self):
        if(self.fitness < self.bestFitness):
            self.bestFitness = self.fitness
            self.bestPosition = self.position