from graph import Graph, graph_from_file
from kruskal_min_power import*

def routes_out(x):
     ''' Cette fonction permet de générer le fichier route out sous forme de fichier texte.
     Ce fichier à T lignes (nombre de trajets étudiés). Chaque ligne est composé de deux entiers ou floatants
     respectivement la puissance minimale pour parcourir la route et son utilité.

        Args: x(int): numéro du fichier routes.x.in
        returns : None
        génère fichier routes.x.out
    '''

     filename="input/routes."+ str(x) + ".in"
     filename_new="output/routes."+ str(x) + ".out"
     network = "input/network." + str(x)+ ".in"
    
     g= graph_from_file(network)
     g_mst=kruskal(g)
    
     profondeurs, parents = parents_profondeurs(1, g_mst)
     res=[]

     with open(filename) as file: #on ouvre le fichier
             ligne1=file.readline().split()
             nb_trajets=int(ligne1[0])

             for i in range(nb_trajets):
                 lignei=file.readline().split() # i eme ligne du fichier file 
                 utilite=str(lignei[2]) #on récupère l'utilité
                 src=int(lignei[0]) # Premier noeud à relier 
                 dest=int(lignei[1]) # Second noeud à relier

                 chemin, p_min = min_power3(src, dest, g_mst, parents, profondeurs)

                 res.append((p_min, utilite))

     with open(filename_new, "w") as file :
         for  el in res :
             puissance = el[0]
             utilite = el[1]

             file.write(str(puissance)+ " " + utilite + "\n")


for i in range(1,11):

    print(routes_out(i))
 

    


        

