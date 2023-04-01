from graph import Graph, graph_from_file
from kruskal_min_power import*

#enlever les camions inutiles (plus cher que d'autres camion avec une plus grande puissance)


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
    ''' Cette fonction permet de renvoyer le catalogue de camion sous forme de liste à partir du fichier trucks.x.out.

        Args: x(int): numéro du fichier trucks.x.in
        returns : res(list) : liste des couples (puissance, cout) de chaque camion du fichier trucks
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

def catalogue_utile(x):
    '''Cette fonction enlève les camions "inutiles", c'est-à-dire ceux ayant une puissance 
    inférieure à un autre camion moins cher. Elle crée un fichier text trucks.x.out avec les camions utiles
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

def appariement(x_trucks,y_routes):
    '''Cette fonction choisit le camion le moins cher pour chaque trajet du fichier routes.y_routes_out.out
    args : 
        x_trucks(int):
        y_routes(int)

    returns :
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

print(appariement(2,4))






    
