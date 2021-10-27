#Num Atoms


c = 6.022*10**23

def num_atoms(g,aw=196.97):
    m = g/aw
    z = m*c
    return z
x = num_atoms(10)

print(x)