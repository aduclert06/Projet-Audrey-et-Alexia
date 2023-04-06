

from graph import Graph, graph_from_file
from time import*
from kruskal_min_power import*

''' Estimation de temps de la question 10'''

'''on estime le temps nécessaire pour calculer (à l’aide du code développé dans la séance 1) la
#puissance minimale (et le chemin associé) sur l’ensemble des trajets pour chacun des fichiers routes.x.in
#donnés.'''



######On définit une fonction qu'on peut appliquer à chaque fichier routes######

'''Dans l'ensemble de ces fonctions l'argument sera toujours le même :
Args: x(int): numéro du fichier routes.x.in'''

def temps(x):

    filename="input/routes."+ str(x) + ".in"
    network = "input/network." + str(x)+ ".in"

    with open(filename) as file: #on ouvre le fichier
            ligne1=file.readline().split()
            nb_trajets=int(ligne1[0])
        
        
            ligne2=file.readline().split() # 2 eme ligne du fichier file 
            src2=int(ligne2[0]) # Premier noeud à relier 
            dest2=int(ligne2[1]) # Second noeud à relier

            ligne3=file.readline().split() # 3 eme ligne du fichier file 
            src3=int(ligne3[0]) # Premier noeud à relier 
            dest3=int(ligne3[1]) # Second noeud à relier

            ligne4=file.readline().split() # 4 eme ligne du fichier file 
            src4=int(ligne4[0]) # Premier noeud à relier 
            dest4=int(ligne4[1]) # Second noeud à relier



    g = graph_from_file(network)

    #on le teste sur les 3 premières lignes du fichier et on fait une moyenne de ces 3 temps pour ensuite
    #la multiplier par le nombre de trajet

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

#on se rend compte sur les fichiers 1 et 2 qu'on a une durée de plusieurs jours, ce qui est trop long.
#Pour les fichiers plus gros (routes 3,4...), python execute trop de récursions.
#Il faut donc améliorer notre fonction min_power


''' On reprend les estimations de temps de la question 10'''



''' On définit une fonction qui calcule le temps pour trouver les trajets sur un fichier route avec la deuxième méthode'''

def temps2(x):

    filename="input/routes."+ str(x) + ".in"
    network = "input/network." + str(x)+ ".in"

    with open(filename) as file: #on ouvre le fichier
            ligne1=file.readline().split()
            nb_trajets=int(ligne1[0])
        
        
            ligne2=file.readline().split() # 2 eme ligne du fichier file 
            src2=int(ligne2[0]) # Premier noeud à relier 
            dest2=int(ligne2[1]) # Second noeud à relier

            ligne3=file.readline().split() # 3 eme ligne du fichier file 
            src3=int(ligne3[0]) # Premier noeud à relier 
            dest3=int(ligne3[1]) # Second noeud à relier

            ligne4=file.readline().split() # 4 eme ligne du fichier file 
            src4=int(ligne4[0]) # Premier noeud à relier 
            dest4=int(ligne4[1]) # Second noeud à relier



    g = graph_from_file(network)
    g1=kruskal(g)

    debut2 = perf_counter()
    min_power2(g1,src2,dest2)
    fin2 = perf_counter()
    tmp2= fin2 - debut2


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

    return ("Le temps pour calculer l'ensemble des trajets du fichier routes avec la deuxième fonction", str(x), "est",temps_routes, "s")

#Le temps pour calculer l'ensemble des trajets a été réduit à 2h pour les premiers network 1 et 2.
#Le programme a du mal à calculer les résultats pour les plus gros graphes. En effet, comme on choisit de mettre la
#destination comme racine de notre arbre, on change de profondeurs et de parents pour chaque chemin
#On perd donc trop de temps à calculer à chaque fois parents et profondeurs.

#On code donc une troisième fois min_power afin de n'avoir à faire les programmes kruskal et parents_profondeurs,
#une seule fois par graphe

''' On définit une fonction qui calcule le temps pour trouver les trajets sur un fichier route avec la troisième méthode
comme indiqué dans la séance 3'''

def temps3(x):

    filename="input/routes."+ str(x) + ".in"
    network = "input/network." + str(x)+ ".in"

    with open(filename) as file: #on ouvre le fichier
            ligne1=file.readline().split()
            nb_trajets=int(ligne1[0])
        
        
            ligne2=file.readline().split() # 2 eme ligne du fichier file 
            src2=int(ligne2[0]) # Premier noeud à relier 
            dest2=int(ligne2[1]) # Second noeud à relier
        

            ligne3=file.readline().split() # 3 eme ligne du fichier file 
            src3=int(ligne3[0]) # Premier noeud à relier 
            dest3=int(ligne3[1]) # Second noeud à relier

            ligne4=file.readline().split() # 4 eme ligne du fichier file 
            src4=int(ligne4[0]) # Premier noeud à relier 
            dest4=int(ligne4[1]) # Second noeud à relier


    g = graph_from_file(network)
    g1=kruskal(g)
    
    po, pa = parents_profondeurs(1, g1)

    debut2 = perf_counter()
    a=min_power3(src2,dest2, g1, pa, po)
    fin2 = perf_counter()
    tmp2= fin2 - debut2
    


    debut3 = perf_counter()
    b=min_power3(src3,dest3, g1, pa, po)
    fin3 = perf_counter()
    tmp3= fin3 - debut3
    
    

    debut4 = perf_counter()
    c=min_power3(src4,dest4, g1, pa, po)
    fin4 = perf_counter()
    tmp4= fin4 - debut4
    

    tmp_moy = (tmp2 + tmp3 +tmp4)/3
    temps_routes = tmp_moy*nb_trajets

    return (temps_routes)

''' On définit une fonction pour donner le temps d'éxecution de la fonction kruskal'''

def temps_krusk(x):
    network = "input/network." + str(x)+ ".in"
    g=graph_from_file(network)

    debut = perf_counter()
    kruskal(g)
    fin = perf_counter()
    tmp = fin- debut

    return("Le temps de Kruskal est", tmp, "s")

''' On définit une fonction pour donner le temps d'éxecutionde parents_profondeurs et de kruskal'''


def temps_kruskal_prof_par(x):
    network = "input/network." + str(x)+ ".in"
    g=graph_from_file(network)

    debut = perf_counter()
    g_mst=kruskal(g)
    parents_profondeurs(1,g_mst)
    fin = perf_counter()
    tmp = fin- debut

    return(tmp)


def temps_total(x) :
    tmpmin = temps3(x)
    t_k_par_prof= temps_kruskal_prof_par(x)
    total = tmpmin + t_k_par_prof
    return ("Le temps pour calculer l'ensemble des trajets du fichier routes au total du fichier route", str(x), "est",total, "s")





''' Comparaison regroupe nos fonctions de temps et nous permet de les appeler facilement'''

def comparaison(x):
    #print(temps(x))
    #print(temps3(x))
    #print(calcul(x))
    #print(temps_kruskal_prof_par(x))
    
    print(temps_total(x))

for i in range (1,10):
    print(comparaison(i))

'''Conclusion : On trouve un résultat de l'ordre de la minute, on a lancé plusieurs fois le programme, on trouve
au maximum un temps inférieur à 200s '''

