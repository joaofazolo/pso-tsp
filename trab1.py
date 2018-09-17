import math
import numpy
from swarm import Swarm

#Leitura do arquivo de coordenadas
def tsp_reader(file):
    line = ""
    while(line != "EOF"):
        line = file.readline().strip()
        if(line.split(": ")[0] == "DIMENSION"):
            size = int(line.split(": ")[1])
            m = []
        if(line.split(": ")[0] == "NODE_COORD_SECTION"):
            for i in range(0,size):
                node_line = file.readline().split()
                city_num = int(node_line[0])
                city_x = float(node_line[1])
                city_y = float(node_line[2])
                m.append([])
                m[i].append(city_num)
                m[i].append(city_x)
                m[i].append(city_y)
    return m


def create_matrix(arr):
    mat = [[0 for x in range(len(arr))] for y in range(len(arr))]
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            mat[i][j] = mat[j][i] = calc_distancia(arr[i][1],arr[i][2],arr[j][1],arr[j][2])
    
    return mat


def calc_distancia(x1,y1,x2,y2):
    return round(math.sqrt(pow(x1-x2,2)+pow(y1-y2,2)),2)
    

def func_obj(matriz,permutacao):
    custo = 0
    for i in range(0,len(permutacao)-1):
        j = i+1
        custo = custo + matriz[permutacao[i]-1][permutacao[j]-1]

    custo = custo + matriz[permutacao[-1]-1][permutacao[0]-1]

    return custo


tspFile = open("29.tsp","r")
# print tsp_reader(tspFile)


data = tsp_reader(tspFile)
matrix = create_matrix(data)
permutacao = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# print func_obj(matrix,permutacao)
s = Swarm(5,2,1,1)
s.particles[0].setPosition([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
s.particles[0].evaluateFitness(matrix)
print s.particles[0].speed
s.updateSpeeds()
print s.particles[0].speed
print s.particles[0].position
s.particles[0].swap([2,5])
print s.particles[0].position


# print s.particles[1].getId()

# print matrix
