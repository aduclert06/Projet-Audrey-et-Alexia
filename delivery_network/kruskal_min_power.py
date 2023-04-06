from graph import Graph, graph_from_file
from time import*

def find(parent, x):
    '''fonction permettant de trouver le parent de x, qui est donc le représentant de l'ensemble auquem il appartient.
    Fonction utile dans l'algorithme de Kruskal
    args: 
        parent(list): liste répertoriant les parents de chaque noeud. le parent de i est parent[i]
        x(int): noeud dont on veut trouver le parent
    returns:
        parent[x](int): parent de x

    '''
    if parent[x] != x:
        parent[x]=find(parent, parent[x])
    return parent[x]
    
    

def kruskal(g):
    '''Algorithme de Kruskal. transforme un graphe dont les arêtes sont pondérés en un arbre couvrant minimal (on ne garde que les chemins de poids minimal entre les noeuds)
    args :
        g(objet de la classe Graph): graphe dont on veut l'arbre couvrant minimal
    returns:
        g_mst(objet de la classe Graph): arbre couvrant minimal du graphe g'''

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
    '''Cette fonction est appelé dans la fonction parents_profondeurs. C'est elle qui fait les calculs.
    et modifie les deux dictionnaires pour renvoyer les dictionnaires parents et profondeurs.
    args :
        node(int): noeud dont on part pour s'enfoncer dans l'arbre
        prof(int): profondeur de node
        parent(int): parent de node
        g(objet de la classe graphe): graphe dont est issu node
        profondeurs(dictionbnaire): dictionnaire des profondeurs à modifier
        parents(dictionnaire): dictionnaires de parents à modifier 

    returns :
        profondeurs(dictionbnaire): dictionnaire des profondeurs ayant pour clefs les noeuds de l'arbre et pour valeurs les profondeurs associées
        parents(dictionnaire): dictionnaires de parents à modifier ayant pour clefs les noeuds de l'arbre et pour valeurs leur parent

'''
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
    '''cette fonction renvoie 2 dictionnaires dont les clefs sont les noeuds de l'arbre :
un dictionnaire des profondeurs et un dictionnaires des parents.
Args :
    racine(int): racine de l'arbre que l'on choisit
    g(objet de la classe graphe): arbre dont on veut connaitre les profondeurs et les parents de ses noeuds.
Returns :  
    parents(dictionnaire): dictionnaire des parents des noeuds du graphe 
        (les noeuds sont les clefs, les parents les valeurs associées)
    profondeurs(dictionnaire): dictionnaire des profondeurs des noeuds du graphe 
        (les noeuds sont les clefs, les profondeurs les valeurs associées) 

    '''
    profondeurs={} #on initialise
    parents ={} # on initialise

    profondeur(racine, 0, -1, g, profondeurs, parents) #par défault la racine à une profondeur de 0 et son parent est -1
    return profondeurs, parents



def min_power2 (g_mst, src, dest):
    '''Cette fonction calcule le chemin de puissance minimal entre src et dest en utilisant les propriétés de l'arbre couvrant minimal.
    Ici, on prend pour racine du graphe la destination (dest). On calcule la profondeur de la source (src).
    Il suffit alors de rejoindre la source en remontant de parent en parent le nombre de fois nécessaire (c'est à dire
    de la profondeur de dest).

    Args :
        g_mst(objet de la classe graphe): arbre couvrant minimal considéré
        src(inbt): noeud source
        dest(int):noeud destination
    returns :
        chemin(liste) : renvoie le chemin reliant src à dest qui est donc par les propriétés de l'arbre couvrant minimal
        le chemin le plus économique en puissance.
    '''
    #g_mst=kruskal(g) #on récupère l'arbre minimal couvrant
    #print(g_mst)
    chemin=[src]
    profondeurs, parents = parents_profondeurs(dest,g_mst) #Par défaut on prend la destination comme racine
    p_src = profondeurs[src]# on calcule la profondeur de la source par rapport à la dest
    for i in range (p_src):#On relie alors src à dest car le trajet est direct par les propriétés des arbres couvrants minimum
        chemin.append(parents[src])
        src= parents[src]

    return chemin

''' On essaye d'optimiser min_power2 qui nous donne un résultat en 2h'''

def min_power3(src, dest, g_mst, parents, profondeurs):
    '''Le principe de cette fonction est de trouver le plus proche parent commun de dest et de src.
    On crée deux chemins, le premier relier la src à ce parent, le deuxième la destination au parent commun. 
    On concatène ensuite les deux chemins. On sait que ce chemin est unique et le 
    plus économique en puissance par priopriété de kruskal
    
    Args :
        src(int): noeud source
        dest(int): noeud destination
        parents(dictionnaire): dictionnaire des parents des noeuds du graphe 
        (les noeuds sont les clefs, les parents les valeurs associées)
        profondeurs(dictionnaire): dictionnaire des profondeurs des noeuds du graphe 
        (les noeuds sont les clefs, les profondeurs les valeurs associées) 
    returns :
        
        chemin(list): liste contenant les noeuds composant le chemin le plus économique en
        puissance entre src et dest
        p_min(int): puissance minimale que le camion doit posséder pour rejoindre les deux noeuds.'''

    #initialisation des chemins
    chemin1=[src] 
    chemin2=[dest]
    chemin=[]
    #pour trouver le parent commun, on a besoin de calculer les profondeurs de src et dest

    prof_dest= profondeurs[dest]
    prof_src= profondeurs[src]

    #Cas de bord où l'on veut relier src à elle-même
    if src == dest :
        return ([src],0)
    
    #le but est d'amener le noeud dont la profondeur est la plus grande
    #au niveau de la profondeur de l'autre noeud, pour remonter ensuite en même temps jusqu'au parent commun
    
    #disjonction de cas


    if prof_src>prof_dest :
        while prof_src!= prof_dest :
            src=parents[src]
            if src==dest :
                chemin1.append(src)
                chemin2=[]
                break
            else :
                prof_src = profondeurs[src]
                chemin1.append(src)


    if prof_dest>prof_src :
        while prof_src!= prof_dest :
            dest=parents[dest]
            if src==dest:
                chemin2.append(dest)
                chemin1=[]
                break
            
            else :
                prof_dest = profondeurs[dest]
                
                chemin2.append(dest)
    
    #Une fois que les noeuds sont à la même hauteur, il se peut que le parent commun soit déjà trouvé
    #Le chemin le plus économique est donc trouvé
    if parents[src]==parents[dest] and src!=dest :
        src1=parents[src]
        
        chemin1.append(src1)

    #Une fois que les noeuds sont à la même hauteur, on remonte jusqu'au parent commun
    while parents[src]!=parents[dest]:
        chemin1.append(parents[src])
        chemin2.append(parents[dest])
        src=parents[src]
        dest=parents[dest]
    

        chemin1.append(parents[src])

        

    chemin2.reverse()
    
    chemin = chemin + chemin1 + chemin2
    
   
        
    #On cherche la puissance à renvoyer
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
network2= "input/network.2.in"
g1 = graph_from_file(network2)
g2=kruskal(g1)
#print(g2)
po, pa = parents_profondeurs(1, g2)
#print(po,pa)
#print(po[3])

#print(min_power2(g1,3,8))
#print(min_power3(6,6, g2, pa, po))

#print(g1)
#print(kruskal(g1))

#rendu 06/04/23