from particle import Particle

class Swarm:
    bestPosition = []
    bestFitness = 99999
    particles = []

    def __init__(self,nParticles,inertialC,acceleration1,acceleration2):
        self.inertialC = inertialC
        self.acceleration1 = acceleration1
        self.acceleration2 = acceleration2
        for i in range(nParticles):
            p = Particle(5)
            p.setId(i)
            self.particles.append(p)
    
    def updateSpeeds(self):
        for particle in self.particles:
            newSpeed = self.inertialC*particle.getSpeed()
            particle.updateSpeed(newSpeed)

