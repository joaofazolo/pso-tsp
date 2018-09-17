import random

#Classe particula
class Particle:
    bestPosition = []
    bestFitness = 999999
    position = []
    fitness = 999999
    speed = []


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
    
    #Atualiza velocidade
    def updateSpeed(self,acceleration1,acceleration2,globalBest):
        oldSpeed = self.speed
        self.speed.append(oldSpeed)
        dice = random.random()
        r1 = random.random()/2
        r2 = random.random()/2
        if(r1+acceleration1 >= dice):
            
            self.speed.append()
        self.speed.append(oldSpeed)
        self.speed.append(oldSpeed)


    def getSpeed(self):
        return self.speed
    
    #Operacao para realizar o swap de duas cidades na permutacao (1,2)
    def swap(self,swap):
        aux = self.position[swap[0]]
        self.position[swap[0]] = self.position[swap[1]]
        self.position[swap[1]] = aux

    def diff(self,p):
        diff = []
        for i in range(len(p.position)):
            print str(p.position[i]) + " , " + str(self.position[i])
            if(p.position[i] != self.position[i]):
                print "teste"
                for j in range(len(self.position)):

                    if(p.position[i] == self.position[j]):
                        if([j,i] not in diff):
                            diff.append([i,j])
        return diff
                
