from sys import argv

def brute_force(s,M,L):
    if(len(L) == 0):
        return M[s[-1]-1][s[0]-1]

    vals = []
    for i in range(len(L)):
        v = M[s[-1]-1][L[i]-1] + brute_force(s + [L[i]],M,L[:i] + L[i+1:])
        vals.append(v)
        
    return min(vals)