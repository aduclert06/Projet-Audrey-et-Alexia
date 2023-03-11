#https://github.com/aduclert06/Projet-Audrey-et-Alexia.git

from graph import Graph, graph_from_file
from time import*

'''on estime le temps nécessaire pour calculer (à l’aide du code développé dans la séance 1) la
#puissance minimale (et le chemin associé) sur l’ensemble des trajets pour chacun des fichiers routes.x.in
#donnés.'''



######fOn définit une fonction qu'on peut appliquer à chaque fichier routes######
def temps(x):

    filename="input/routes."+ str(x) + ".in"
    network = "input/network." + str(x)+ ".in"

    with open(filename) as file: #on ouvre le fichier
            ligne1=file.readline().split()
            nb_trajets=int(ligne1[0])
        
        
            ligne2=file.readline().split() # i eme ligne du fichier file 
            src2=int(ligne2[0]) # Premier noeud à relier 
            dest2=int(ligne2[1]) # Second noeud à relier

            ligne3=file.readline().split() # i eme ligne du fichier file 
            src3=int(ligne2[0]) # Premier noeud à relier 
            dest3=int(ligne2[1]) # Second noeud à relier

            ligne4=file.readline().split() # i eme ligne du fichier file 
            src4=int(ligne2[0]) # Premier noeud à relier 
            dest4=int(ligne2[1]) # Second noeud à relier



    g = graph_from_file(network)

    debut2 = perf_counter()
    g.min_power(src2,dest2)
    fin2 = perf_counter()
    tmp2= fin2 - debut2


    debut3 = perf_counter()
    g.min_power(src3,dest3)
    fin3 = perf_counter()
    tmp3= fin3 - debut3
    

    debut4 = perf_counter()
    g.min_power(src4,dest4)
    fin4 = perf_counter()
    tmp4= fin4 - debut4

    tmp_moy = (tmp2 + tmp3 +tmp4)/3
    temps_routes = tmp_moy*nb_trajets

    return ("Le temps pour calculer l'ensemble des trajets du fichier routes", str(x), "est", temps_routes, "s")

#print(temps(1))
#print(temps(2))

#on se rend compte sur les fichiers 1b et 2 qu'on a une durée de plusieurs heures, ce qui est trop long.
#Pour les fichiers plus gros (routes 3,4...), python execute trop de récursions.
#Il faut donc améliorer notre fonction min_power



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
            
    aretes.sort(key=lambda x : x[2])#tri de la liste
    

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
        else :
            g_mst.add_edge(a, b , p)
    

    return g_mst