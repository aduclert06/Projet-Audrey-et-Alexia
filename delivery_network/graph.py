class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        self.nb_edges +=1
        

        if node1 in self.graph.keys(): #on regarde si le noeud 1 est dans le dictionnaire (c'est-à-dire le graphe)    
             self.graph[node1].append((node2, power_min, dist))#s'il y est on complète le dictionnaire en ajoutant l'arrêtre entre 1 et 2 à la clé correspondante
                
            
        else:
            key, value = node1, (node2, power_min, dist)#sinon on crée une nouvelle clé avec le noeud 1
            self.graph[key] = [value]#et on ajoute l'arrêt
            
        if node2 in self.graph.keys():#on fait de même pour le noeud 2
            self.graph[node2].append((node1, power_min, dist))
        else:
            key, value = node2, (node1, power_min, dist)
            self.graph[key] = [value]
            
        return self.graph
    
    def parcours_profondeur(self, node, chemin, dest, power, visited_node):#on fait une fonction récursive pour voir s'il l'on peut rejoindre la destination avec la puissance donnée sur le principe du parcours en profondeur
            
            if  node == dest :
                return chemin

            for voisin in self.graph[node]:#on regarde les voisins du noeud
                
                if voisin[1] <= power and not visited_node[voisin[0]]:#si la puissance pour rejoindre le voisin est inférieure à celle donnée, alors on peut passer et on vérifie qu'on n'a pas déjà visité ce noeud
                    
                    visited_node[voisin[0]]=True#on marque que le noeud a été visité
                        
                    resultat = self.parcours_profondeur(voisin[0], chemin+[voisin[0]], dest, power, visited_node)#sinon on continue l'exploration en profondeur, en ajoutant le voisin au chemin potentiel
                    if resultat is not None:
                        return resultat
            return None  #s'il ne trouve pas de chemin, on renvoie NONE

    def get_path_with_power(self, src, dest, power):
        chemin =[src]#on initialise le chemin par son début qui est la source, src
        #pour ce programme on reprend le principe du parcours en profondeur des composantes connexes, auquel on va ajouter la condition de puissance
        visited_node = {node : False for node in self.nodes}#on crée un dictionnaire notifiant le statut des noeuds(visité ou non)
        visited_node[src]=True#le départ, src est forcément visité donc on le met en TRUE

        res = self.parcours_profondeur(src, chemin, dest, power, visited_node)#sinon on renvoie le premier chemin trouvé
        return  res
    
    def connected_components(self):
        liste_composantes = []#On crée la liste vide des composante, que l'on va compléter au long du programme
        visited_node = {node : False for node in self.nodes}#on crée un dictionnaire qui indique si un noeud a été visité ou non

        def parcours_profondeur(node):#on crée une fonction récurvise qui va parcourir toute la composante connexe
            composante = [node]#La composante est constitué d'un premier noeud
            for voisin in self.graph[node]:#on va visiter les voisins de ce noeud
                voisin = voisin[0]
                if not visited_node[voisin]:#si le noeud n'a pas déjà été visité
                    visited_node[voisin] = True#on change son statut comme visité
                    composante += parcours_profondeur(voisin)#on va regarder les voisins de ce noeud, que l'on ajoute de manière récursive à la composante connexe
            return composante #on renvoie la composante
        for node in self.nodes: #on applique le parcours le parcours en profondeur à tous les noeuds du graphe pour trouver les compposantes connexes
            if not visited_node[node]:
                liste_composantes.append(parcours_profondeur(node))#on ajoute les composantes connexes à la liste des composantes
        return liste_composantes
        
    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        #on fait une recherche dichotomique sur la puissance

        puissances=[]#initialisation de la liste des puissances
        for node in self.nodes:#Création de la liste des puissances en parcourant toutes les arrêtes du graphe
            for e in self.graph[node] :
                puissances.append(e[1])
        
        set(puissances)
        #print(puissances)
        puissances_unique = list(set(puissances))#on enlève les doublons
        #recherche dichotomique du chemin le plus économique en puissance
        puissances_unique.sort()#tri de la liste
        a=0
        b=len(puissances_unique)-1
        m=(a+b)//2
        
        while a<=b :
            p_tmp=puissances_unique[m]
            p_ant=puissances_unique[m-1]
            
            if self.get_path_with_power(src, dest, p_tmp)==None :
                a=m+1
            elif self.get_path_with_power(src, dest, p_ant)==None :
                break
            
            else:
                b=m-1
            m=(a+b)//2

        chemin_eco=self.get_path_with_power(src, dest, p_tmp)
        p_min=p_tmp
        return (chemin_eco, p_min)
    
    

    




def graph_from_file(filename): #fonction qui crée un graphe qui sera alors du type de la classe graph
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename) as file: #on ouvre le fichier
        ligne1=file.readline().split()
        n=int(ligne1[0])
        m=int(ligne1[1])
        nodes=[i for i in range(1, n+1)]
        G=Graph(nodes)
        for i in range(m):
            lignei=file.readline().split() # i eme ligne du fichier file 
            node1=int(lignei[0]) # Premier noeud à relier 
            node2=int(lignei[1]) # Second noeud à relier
            power_min=int(lignei[2]) # Puissance de l'arrête
            if len(lignei)>3: # cas où il y a une distance d'une arrête
                dist=int(lignei[3]) # Distance de l'arête 
                G.add_edge(node1, node2, power_min, dist)
            else:
                G.add_edge(node1, node2, power_min)
    return G

    

