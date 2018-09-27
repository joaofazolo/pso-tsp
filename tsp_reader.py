from sys import argv
import math

inf = 999999

#Leitura do arquivo de coordenadas, retorna vetor de cidades
def tsp_reader(name):
    try:
        file = open(name+".tsp","r")
    except:
        raise Exception("Arquivo nao encontrado")
    
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
    return create_matrix(m)


    #Cria matriz de distancias a partir do vetor de cidades
def create_matrix(arr):
    mat = [[inf for x in range(len(arr))] for y in range(len(arr))]
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            mat[i][j] = mat[j][i] = calc_distancia(arr[i][1],arr[i][2],arr[j][1],arr[j][2])
    
    return mat

#Calcula distancia entre duas cidades
def calc_distancia(x1,y1,x2,y2):
    return round(math.sqrt(pow(x1-x2,2)+pow(y1-y2,2)),2)