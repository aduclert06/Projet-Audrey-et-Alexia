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

    aretes=[]#initialisation de la liste des aretes
    
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



'''On code les fonctions pour trouver le plus court chemin dans un arbre minimal couvrant obtenu avec kruskal'''

#on code une fonction qui calcule les parents et les profondeurs des noeuds de l'arbre

def profondeur(node, prof, parent, g, profondeurs, parents):
        profondeurs[node]= prof #profondeurs est un dictionnaire, on ajoute donc la profondeur correspondante au noeud
        parents[node]= parent #parents est un dictionnaire, on ajoute le parent du noeud 
        #print(parents)

        for voisin in g.graph[node] :
            if voisin[0] != parent : #on cherche à s'enfoncer dans l'arbre donc on ne veut pas retourner vers le parent
                profondeur(voisin[0], prof +1, node, g, profondeurs, parents)#on réitère donc la fonction en prenant pour
                #nouveau parent, le noeud voisin, on s'enfonce dans l'arbre, donc on augmente la profondeur de 1

#on code une fonction qui renvoie 2 dictionnaires dont les clefs sont les noeuds de l'arbre :
#un dictionnaire des profondeurs et un dictionnaires des parents
def parents_profondeurs(racine, g) :
    profondeurs={} #on initialise
    parents ={} # on initialise

    profondeur(racine, 0, -1, g, profondeurs, parents) #par défault la racine à une profondeur de 0 et son parent est -1
    return profondeurs, parents

def min_power2 (g_mst, src, dest):
    #g_mst=kruskal(g) #on récupère l'arbre minimal couvrant
    #print(g_mst)
    chemin=[src]
    profondeurs, parents = parents_profondeurs(dest,g_mst)
    p_src = profondeurs[src]
    for i in range (p_src):
        chemin.append(parents[src])
        src= parents[src]

    return chemin

network = "input/network.02.in"
g1 = g = graph_from_file(network)
g2=kruskal(g1)

#print(min_power2(g1,2,8))

#print(g1)
#print(kruskal(g1))

''' On reprend les estimations de temps de la question 10'''


######fOn définit une fonction qu'on peut appliquer à chaque fichier routes######
def temps2bis(x):

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

            #ligne4=file.readline().split() # i eme ligne du fichier file 
            #src4=int(ligne2[0]) # Premier noeud à relier 
            #dest4=int(ligne2[1]) # Second noeud à relier



    g = graph_from_file(network)
    g1=kruskal(g)

    debut2 = perf_counter()
    min_power2(g1,src2,dest2)
    fin2 = perf_counter()
    tmp2= fin2 - debut2#


    debut3 = perf_counter()
    min_power2(g1,src3,dest3)
    fin3 = perf_counter()
    tmp3= fin3 - debut3
    

    #debut4 = perf_counter()
    #min_power2(g1, src4,dest4)
    #fin4 = perf_counter()
    #tmp4= fin4 - debut4

    tmp_moy = (tmp2 + tmp3 )/2
    temps_routes = tmp_moy*nb_trajets
    return(temps_routes)

def temps2(x):

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
    g1=kruskal(g)

    debut2 = perf_counter()
    min_power2(g1,src2,dest2)
    fin2 = perf_counter()
    tmp2= fin2 - debut2#


    debut3 = perf_counter()
    min_power2(g1,src3,dest3)
    fin3 = perf_counter()
    tmp3= fin3 - debut3
    

    debut4 = perf_counter()
    min_power2(g1, src4,dest4)
    fin4 = perf_counter()
    tmp4= fin4 - debut4

    tmp_moy = (tmp2 + tmp3 +tmp4)/3
    temps_routes = tmp_moy*nb_trajets

    #"Le temps pour calculer l'ensemble des trajets du fichier routes avec la deuxième fonction", str(x), "est",
    #"s"


    return (temps_routes)

def calcul(x) :
    t2=temps2bis(x)
    t3=temps2(x)

    filename="input/routes."+ str(x) + ".in"
    network = "input/network." + str(x)+ ".in"

    with open(filename) as file: #on ouvre le fichier
            ligne1=file.readline().split()
            nb_trajets=int(ligne1[0])
    a = (6/(nb_trajets)*(t2-t3)+3*t3-2*t2)

    return ((6/(nb_trajets)*(t2-t3)+3*t3-2*t2))

def ioka(x):
    print(temps(x))
    print(temps2(x))
    print(calcul(x))

print(ioka(2))