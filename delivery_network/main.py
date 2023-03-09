from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)
print(g)

def find(parent, x):
    while parent[x]!= x:
        x=parent[x]
    return x
    

def kurskal(g):
    g_mst=Graph() #on initialise le graphe à renvoyer

    aretes=[]#initialisation de la liste des puissances
    
    for node in nodes:#Création de la liste des puissances en parcourant toutes les arrêtes du graphe
        for e in g[node]:
            ar = e.insert(0,node) #on crée l'arête de la forme (noeud1, noeud2, power, dist)
            aretes.append(ar)# on ajoute l'arête à la liste des arêtes
    aretes.sort(key=lambda x : x[1])#tri de la liste

    parent = list(range(g.nb_nodes)) #on initialise la liste représentant les sous-ensembles, chaque noeud est parent de lui-même à l'initialisation

    for ar in aretes :
        #l'objectif de la liste parent est d 'avoir un lien entre la position d'un noeud et le sous ensemble auquel il appartient, chaque sous-sensemble
        #est représenté par un noeud référent appelé parent.
        #On renome donc les noeuds pour que le nom du noeud à l'initialisation corresponde à son indice dans la liste parent
        #C'est pour cela qu'on soustrait 1 à chaque noeud
        n1-1 = ar[0] 
        n2-1=ar[1]
        p=ar[2] #puissance de l'arête
        if len(ar)>3:#si l'arête a une puissance, on l'ajoute
            dist=ar[3]
        
        
        

    mst=[]

    
