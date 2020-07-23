e = "Emma"
g = "Gunnar"
t = "Tie"

def parse_data():
    G = [int(i) for i in input().split()]
    E = [int(i) for i in input().split()]
    G1,G2 = (G[0],G[1]), (G[2],G[3])
    E1,E2 = (E[0],E[1]), (E[2],E[3])
    g_average,e_average = tot_average(G1,G2),tot_average(E1,E2)
    return g_average - e_average

def tot_average(a,b):
    return ((a[0]+a[1])/2) + ((b[0]+b[1])/2)

def run():
    value = parse_data()
    if value < 0:
        print(e)
    elif value > 0:
        print(g)
    else:
        print(t)

if __name__=="__main__":
    run()
