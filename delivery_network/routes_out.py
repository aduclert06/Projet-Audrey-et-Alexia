from graph import Graph, graph_from_file
from kruskal_min_power import*

def routes_out(x):

    filename="input/routes."+ str(x) + ".in"
    filename_new="input/routes."+ str(x) + ".out"
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
                src=int(lignei[0]) # Premier noeud à relier 
                dest=int(lignei[1]) # Second noeud à relier

                chemin, p_min = min_power3(src, dest, g_mst, parents, profondeurs)

                res.append(p_min)

    with open(filename_new, "w") as file :
        for  puissance in res :
            file.write(str(puissance) + "\n")

print(routes_out(1))
        

