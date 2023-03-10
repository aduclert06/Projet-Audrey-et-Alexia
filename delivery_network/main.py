#https://github.com/aduclert06/Projet-Audrey-et-Alexia.git
from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.02.in"

g = graph_from_file(data_path + file_name)
print(g)

def find(parent, x):
    while parent[x]!= x:
        x=parent[x]
    return x
    

def kruskal(g):
    g_mst=Graph() #on initialise le graphe à renvoyer
    mst_edges=[]

    aretes=[]#initialisation de la liste des puissances
    
    for node in g.nodes:#Création de la liste des puissances en parcourant toutes les arrêtes du graphe
        for e in g.graph[node]:
            ar = (node,) + e #on crée l'arête de la forme (noeud1, noeud2, power, dist)
            aretes.append(ar)# on ajoute l'arête à la liste des arêtes
            
    aretes.sort(key=lambda x : x[1])#tri de la liste

    #En triant les arêtes par puissance, on est sûr de tester les arêtes donnant l'arbre couvrant minimum

    parent = list(range(g.nb_nodes)) #on initialise la liste représentant les sous-ensembles, chaque noeud est parent de lui-même à l'initialisation

    for ar in aretes :
        #l'objectif de la liste parent est d 'avoir un lien entre la position d'un noeud et le sous ensemble auquel il appartient, chaque sous-sensemble
        #est représenté par un noeud référent appelé parent.
        #On renome donc les noeuds pour que le nom du noeud à l'initialisation corresponde à son indice dans la liste parent
        #C'est pour cela qu'on soustrait 1 à chaque noeud
        n1= ar[0] -1 
        n2=ar[1] -1
        a=ar[0]
        
        
        parent_n1=find(parent, n1)
        parent_n2=find(parent, n2)

        #on regarde si les sommets de l'arête appartiennent au  même sous-ensemble
        #S'ils ont le même parent, ils appartiennent au même sous-ensemble, relier les deux somments formerait un cycle
        #Donc on n'ajoute pas cette arête à l'arbe couvrant de poids minimal
        if parent_n1 != parent_n2 :
            #S'ils n'appartiennent au  même sous ensemble, on fusionne ces ensembles
            parent[parent_n1] = parent_n2 #donc l'ensemble 1 a maintenant pour parent le parent de l'ensemble 2
            
        mst_edges.append(ar)
        
    g_mst = Graph(g.nodes)

    for i in range (0,len(mst_edges)):
        ar=mst_edges[i]
        a=ar[0]
        b=ar[1]
        p=ar[2] #puissance de l'arête
        if len(ar)>3:#si l'arête a une puissance, on l'ajoute
            dist=ar[3]
        g_mst.add_edge(a, b , p, dist)

    return g_mst
        
        

    

    
