#https://github.com/aduclert06/Projet-Audrey-et-Alexia.git

from graph import Graph, graph_from_file
from time import*

'''on estime le temps nécessaire pour calculer (à l’aide du code développé dans la séance 1) la
#puissance minimale (et le chemin associé) sur l’ensemble des trajets pour chacun des fichiers routes.x.in
#donnés.'''




def find(parent, x):
    if parent[x] != x:
        parent[x]=find(parent, parent[x])
    return parent[x]
    
    

def kruskal(g):
    g_mst=Graph() #on initialise le graphe à renvoyer

    mst_edges=[]

    aretes=[]#initialisation de la liste des aretes
    
    for node in g.nodes:#Création de la liste des puissances en parcourant toutes les arrêtes du graphe
        for e in g.graph[node]:
            ar = (node,) + e #on crée l'arête de la forme (noeud1, noeud2, power, dist)
            aretes.append(ar)# on ajoute l'arête à la liste des arêtes
    #print(aretes)
            
    aretes.sort(key=lambda x : x[2])#tri de la liste
    

    #En triant les arêtes par puissance, on est sûr de tester les arêtes donnant l'arbre couvrant minimum

    parent = list(range(g.nb_nodes)) #on initialise la liste représentant les sous-ensembles, chaque noeud est parent de lui-même à l'initialisation

    compt=0 #un arbre a au max nb_nodes -1 arêtes, donc on ajoute une variable compteur

    for ar in aretes :
        #compt +=1
        #if compt == g.nb_nodes :
           # break
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

''' On essaye d'optimiser min_power2 qui nous donne un résultat en 2h'''

def min_power3(src, dest, g_mst, parents, profondeurs):
    chemin1=[src]
    chemin2=[dest]
    chemin=[]
    prof_dest= profondeurs[dest]
    prof_src= profondeurs[src]
    

    if prof_src>prof_dest :
        while prof_src!= prof_dest :
            src=parents[src]
            prof_src = profondeurs[src]
            chemin1.append(src)

    if prof_dest>prof_src :
        while prof_src!= prof_dest :
            dest=parents[dest]
            prof_dest = profondeurs[dest]
            chemin2.append(dest)
    else  :
        while parents[src]!=parents[dest]:
            src=parents[src]
            dest=parents[dest]
            chemin1.append(src)
            chemin2.append(dest)
        chemin1.append(parents[src])
    
        

        chemin2.reverse()
        chemin = chemin + chemin1 + chemin2
    
    puissances = []
    p_min = -1 #si on ne trouve pas de chemin, on renvoie une puissance négative

    for i in range (len(chemin)-1):
        key = chemin[i]
        for e in g_mst.graph[key]:

            if e[0]==chemin[i+1]:
                puissances.append(e[1])
    
    if len(puissances)!=0 :
        p_min=max(puissances)

    
    
    return (chemin, p_min)

'''Données pour tester min_power3'''

network = "input/network.00.in"
g1 = g = graph_from_file(network)
g2=kruskal(g1)
print(g2)
po, pa = parents_profondeurs(1, g1)
#print(po,pa)
#print(po[3])

#print(min_power2(g1,3,8))
print(min_power3(3, 8, g2, pa, po))

#print(g1)
#print(kruskal(g1))