from particle import Particle

#Classe swarm
class Swarm:
    bestPosition = []
    bestFitness = 99999
    particles = []

    def __init__(self,nParticles,acceleration1,acceleration2):
        self.acceleration1 = acceleration1
        self.acceleration2 = acceleration2
        for i in range(nParticles):
            p = Particle()
            p.setId(i)
            self.particles.append(p)
    
    #Atualizada velocidade das particulas
    def updateSpeeds(self):
        for particle in self.particles:
            particle.updateSpeed(self.acceleration1,self.acceleration2,self.bestPosition)

    #Retorna uma particula pelo id
    def getParticle(self,id):
        return self.particles[id]
