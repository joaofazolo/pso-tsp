class Particle:
    bestPosition = []
    bestFitness = 999999
    position = []
    fitness = 999999

    def __init__(self,speed):
        self.speed = speed

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setPosition(self, newPosition):
        self.position = newPosition

    def evaluateFitness(self,matriz):
        permutacao = self.position
        custo = 0
        for i in range(0,len(permutacao)-1):
            j = i+1
            custo = custo + matriz[permutacao[i]-1][permutacao[j]-1]

        custo = custo + matriz[permutacao[-1]-1][permutacao[0]-1]
        self.fitness = custo
    
    def updateSpeed(self,newSpeed):
        self.speed = newSpeed

    def getSpeed(self):
        return self.speed
    
    def swap(self,swap):
        aux = self.position[swap[0]]
        self.position[swap[0]] = self.position[swap[1]]
        self.position[swap[1]] = aux
