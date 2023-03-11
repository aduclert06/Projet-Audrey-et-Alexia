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
            
    aretes.sort(key=lambda x : x[2])#tri de la liste
    print(aretes)

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

    
    print("mst_edges =",  mst_edges)    
    g_mst = Graph(g.nodes)
    print("len mst",len(mst_edges))

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
    print("g_mst =", g_mst)

    return g_mst


from time import*

'''on estime le temps nécessaire pour calculer (à l’aide du code développé dans la séance 1) la
#puissance minimale (et le chemin associé) sur l’ensemble des trajets pour chacun des fichiers routes.x.in
#donnés.'''

######fichier routes 1######
 
filename="input/routes.1.in"
network = "input/network.1.in"

with open(filename) as file: #on ouvre le fichier
        ligne1=file.readline().split()
        nb_trajets1=int(ligne1[0])
        
        
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

debut = perf_counter()
g.min_power(src2,dest2)
fin = perf_counter()
tmp2= fin - debut
print(tmp2)

debut = perf_counter()
g.min_power(src3,dest3)
fin = perf_counter()
tmp3= fin - debut

debut = perf_counter()
g.min_power(src4,dest4)
fin = perf_counter()
tmp4= fin - debut

tmp_moy = (tmp2 + tmp3 +tmp4)/3
temps_routes1 = tmp_moy*nb_trajets1

print ("Le temps pour calculer l'ensemble des trajets du fichier routes 1 est", temps_routes1)

######fichier routes 2######
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



for x in range (1,11):
    print(temps(x))


            
        


#def tmp_route(x):
    #num = str(x)
    #a= "input/routes." + num + ".in"

    #g = graph_from_file(a)
    #n=g.nb_nodes
    #tmps=0
    
    #src=randint(1,n)
    #dest=randint(1,n)

    #debut = perf_counter()
    #g.min_power(src,dest)
    #fin = perf_counter()
    #tmp= fin - debut
    #mps+=tmp
    #tmps_moy=tmps/5
    #return  tmps_moy

#print("temps=", tmp_route(1))







        
        

    

    
