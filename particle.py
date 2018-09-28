import random

#Classe particula
class Particle:
    bestPosition = []
    bestFitness = 9999999999999999
    position = []
    fitness = 9999999999999999
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
    
    def evaluateFitnessBest(self,matriz):
        permutacao = self.bestPosition
        custo = 0
        for i in range(0,len(permutacao)-1):
            j = i+1
            custo = custo + matriz[permutacao[i]-1][permutacao[j]-1]

        custo = custo + matriz[permutacao[-1]-1][permutacao[0]-1]
        self.bestFitness = custo

    #Atualiza velocidade
    def updateSpeed(self,acceleration1,acceleration2,globalBest):
        oldSpeed = self.speed

        newSpeed = []
        
        dice = random.random()

        localComponent = self.diff(self.bestPosition)
        if(localComponent):
            for swap in localComponent:
                r1 = (random.choice(range(0,int((10-((acceleration1*10)-1))))))
                if(float(r1)/10 >= dice):
                    newSpeed.append(swap)

        globalComponent = self.diff(globalBest)
        # print "globalComponent: "+ str(globalComponent)
        if(globalComponent):
            for swap in globalComponent:
                r2 = (random.choice(range(0,int((10-((acceleration2*10)-1))))))
                if(float(r2)/10 >= dice):
                    newSpeed.append(swap)

        self.speed = newSpeed

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
            if(p[i] != self.position[i]):
                for j in range(len(self.position)):

                    if(p[i] == self.position[j]):
                        if([j,i] not in diff):
                            diff.append([i,j])
        return diff
                
    def updateBest(self):
        if(self.fitness < self.bestFitness):
            bestPosition = self.position[:]
            bestFitness = self.fitness
            self.bestFitness = bestFitness
            self.bestPosition = bestPosition