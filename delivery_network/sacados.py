from graph import Graph, graph_from_file
from kruskal_min_power import*

#enlever les camions inutiles (plus cher que d'autres camion avec une plus grande puissance)

#récupérer liste des camions :

def catalogue_from_file_in(x):
    ''' Cette fonction permet de renvoyer le catalogue de camion sous forme de liste à partir du fichier trucks.x.in.

        Args: x(int): numéro du fichier trucks.x.in
        returns : res(list) : liste des couples (puissance, cout) de chaque camion du fichier trucks
    '''

    filename="input/trucks."+ str(x) + ".in"
    res=[]

    with open(filename) as file: #on ouvre le fichier
        ligne1=file.readline().split()
        nb_trucks=int(ligne1[0])
            

        for i in range(nb_trucks):
            lignei=file.readline().split() # i eme ligne du fichier file 
            puissance=int(lignei[0]) # Puissance du camion 
            cout=int(lignei[1]) # coût du camion

            res.append((puissance, cout))
    return(res)


def catalogue_from_file_out(x):
    ''' Cette fonction permet de renvoyer le catalogue de camions utiles sous forme de liste à partir du fichier trucks_utile.x.out.

        Args: x(int): numéro du fichier trucks.x.in
        returns : res(list) : liste des couples (puissance, cout) de chaque camion utile du fichier trucks_utile
    '''

    filename="input/trucks_utile."+ str(x) + ".out"
    res=[]

    with open(filename) as file: #on ouvre le fichier
        ligne1=file.readline().split()
        nb_trucks=int(ligne1[0])
            

        for i in range(nb_trucks):
            lignei=file.readline().split() # i eme ligne du fichier file 
            puissance=int(lignei[0]) # Puissance du camion 
            cout=int(lignei[1]) # coût du camion

            res.append((puissance, cout))
    return(res)

#récupérer les routes sous forme de liste

def routes_from_file_out(x):
    ''' Cette fonction permet de renvoyer le fichier route out sous forme de liste

        Args: x(int): numéro du fichier routes.x.out
        returns : res(list) : liste des couples (puissance min, utilite) de chaque trajet du fichier routes.x.out
    '''

    filename="input/routes."+ str(x) + ".out"
    filenamein="input/routes."+ str(x) + ".in"
    res=[]

    with open(filenamein) as file: #on ouvre le fichier
        ligne1=file.readline().split()
        nb_trajets=int(ligne1[0])

    with open(filename) as file :
            
        for i in range(nb_trajets):
            lignei=file.readline().split() # i eme ligne du fichier file 
            puissance_min=int(lignei[0]) # Puissance minimale pour effectuer le trajet
            utilite=float(lignei[1]) # utilite

            res.append((puissance_min, utilite))
    return(res)

#print(routes_from_file_out(1))

#enlever les camions inutiles du catalogue

def catalogue_utile(x):
    '''Cette fonction enlève les camions "inutiles", c'est-à-dire ceux ayant une puissance 
    inférieure à un autre camion moins cher. Elle crée un fichier text trucks_utile.x.out avec les camions utiles
    args : x(int): numero du fichier trucks
    returns : None

    '''
    catalogue= catalogue_from_file_in(x)

    prix_tmp=catalogue[-1][1]
    catalogue_utile=[catalogue[-1]]

    #la liste est triée par puissance croissante

    for i in range (len(catalogue)-1):
        j=len(catalogue)-i-1 #on parcourt la liste à l'envers

        if catalogue[j-1][1]<catalogue_utile[0][1]: #si le camion est utile on l'ajoute à la liste "catalogue_utile"
            catalogue_utile.insert(0,catalogue[j-1])
            prix_tmp=catalogue[j-1][1]
    
    #Création du fichier text qui sera notre nouveau fichier de référence

    filename_new="input/trucks_utile."+ str(x) + ".out"

    with open(filename_new, "w") as file :
        a=str(len(catalogue_utile))

        file.write(a+"\n")

        for  el in catalogue_utile :
            puissance = el[0]
            cout = el[1]

            file.write(str(puissance)+ " " + str(cout) + "\n")
            

c=[(1000,99),(2000, 294), (3000,365), (4000,382),(5000,295)]

#print(catalogue_utile(0))

#Se rapporter au problème du sac à dos. A chaque route on associe un camion avec une certaine puissance et un certain  prix

def appariement(x_trucks,y_routes):
    '''Cette fonction choisit le camion le moins cher pour chaque trajet du fichier routes.y_routes_out.out
    args : 
        x_trucks(int): numéro du fichier trucks_utile.x_trucks.out
        y_routes(int): numéro du fichier routes.y_routes.out

    returns : appariement (lis) : liste des appariements dont les éléments sont comme suit 
    (puissance camion sélectionné, coût du camion selectionné, utilité de la route à traverser avec le camion sélectionné)
    '''
    catalogue = catalogue_from_file_out(x_trucks)
    routes = routes_from_file_out(y_routes)

    appariement=[]

    for i in range (len(routes)):
        p_min=routes[i][0]



        a=0
        p1=catalogue[a][0]
        if p1 >= p_min:
            el=(p1, catalogue[a][1], routes[i][1])
            appariement.append(el)
        b=len(catalogue)-1
        p2=catalogue[b][0]
        m=(a+b)//2
        pm=catalogue[m][0]
            

        while a<=b :
            
                
            if pm==p_min:
                el=(pm, catalogue[m][1], routes[i][1])
                appariement.append(el)
                
                break

            elif pm<p_min :
                
                a=m+1

            elif pm>p_min and catalogue[m-1][0]<p_min :
                
                el=(pm, catalogue[m][1], routes[i][1])
                
                appariement.append(el)
                break

            elif pm>p_min:
                b=m-1
            
            m=(a+b)//2
            pm=catalogue[m][0]
            


    return(appariement)

#print(appariement(2,4))

#fonctions sac à dos
B = 25*10**9 #budget
B2 = 10000
a= appariement(0, 1)

# Solution approchée - Algorithme glouton
'''rappel : appariement(list) : les éléments sont sous la forme
(puissance camion, coût camion, utilité)'''

def sacados_glouton(budget, appariement):
    '''Cette fonction permet de sélectionner de manière naive les camions et les routes à traverser selon un budget donné B.
    Cette fonction ne prend pas en clmpte les éléments suivants. Elle traite le problème éléments à éléments.
    La solution obtenu n'est donc pas l'optimum
    
        args : 
            budget(int)= le budget de l'entreprise de transport
            appariement(liste) : liste des routes à traversé avec le camion coutant le moins cher pour chaque route
            rappel : appariement(list) : les éléments sont sous la forme
(puissance camion, coût camion, utilité)
        returns : 
            gain(float) = renvoie le gain réalisé par l'entreprise avec cette méthode de sélecton de camion
            selection(list) = renvoie la selection de camions à commander avec leur prix et l'affectation à une route désignée par son utilité
            les éléments de selection sont donc comme suit 
            (puissance camion, coût camion, utilité route affectée au camion) '''

    appariement_tri = sorted(appariement, key=lambda x: x[2]) #on trie les éléments d'appariement selon leur utilité
    #cad selon ce qu'ils peuvent rapporter
    selection = []
    cout_total = 0

    while appariement_tri:
        el = appariement_tri.pop() #on regarde le dernier élement d'appariement qui a donc la plus grand utilité
        if el[1] + cout_total <= budget: #s'il a un cout inférieur au budget
            selection.append(el) #alors on l'ajoute à notre selection
            cout_total += el[1] #on actualise le cout total
    gain = sum([i[2] for i in selection])

    return gain, selection #on revoie le profit et les éléments selectionnés

#print(sacados_glouton(B2, a))


# Solution force brute - Recherche de toutes les solutions
def sacados_force_brute(budget, appariement, selection = []):
    '''2^n solutions, effectue beaucoup trop d'opérations pour les fichiers à traiter.
    Fonction récursive testant toutes les possibilités de selection de camion et renvoyant celle rapportant le plus
        arg :
            budget(int): budget de l'entreprise
            appariement(liste) : liste des routes à traversé avec le camion coutant le moins cher pour chaque route
            rappel : appariement(list) : les éléments sont sous la forme
(puissance camion, coût camion, utilité)
            selection(list) : pour la récursivité, selection des tuples (camion, cout camion, utilité route)
        
        returns :
            profit(float): profit effectué (ce que l'on cherche à maximiser)
            selection(list) : selection des tuples (camion, cout camion, utilité route) renvoyant ke profit max


'''

    if appariement: #on regarde s'il y a toujours des éléments dans la liste
        el1, listeel1 = sacados_force_brute(budget, appariement[1:], selection) #récursivité sans prendre l'élément
        el = appariement[0] 
        if el[1] <= budget: #on regarde si on peut acheter le camion
            el2, listeel2 = sacados_force_brute(budget - el[1], appariement[1:], selection + [el]) 
            #Si c'est le cas on l'ajoute à la selection, on retire le coût du camion au budget et on retire le camion de la liste appariement
            if el1 < el2: #on regarde quelle est la solution optimale (ajouter ou non le camion)
                return el2, listeel2

        
        return el1, listeel1
    else:
        profit= sum([i[2] for i in selection]) #on calcule le profit qui est la somme des utilités

        return profit, selection

B3 = 10
a2=((1,8,10),(2,4,6),(3,6,6))

#print(sacados_force_brute(B3, a2))


 






    
