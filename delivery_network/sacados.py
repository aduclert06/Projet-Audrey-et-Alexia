from graph import Graph, graph_from_file
from kruskal_min_power import*

#enlever les camions inutiles (plus cher que d'autres camion avec une plus grande puissance)


def catalogue_from_file(x):
    ''' Cette fonction permet de renvoyer le catalogue de camion sous forme de liste à partir du fichier trucks.

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

def catalogue_utile(x):
    '''Cette fonction enlève les camions "inutiles", c'est-à-dire ceux ayant une puissance inférieure à un autre camion moins cher.
    args : catalogue(list): liste renvoyée par catalogue_from_file
    returns : catalogue_utile(list): liste des couples (puissance, cout) des camions utiles
    '''
    catalogue= catalogue_from_file(x)

    prix_tmp=catalogue[-1][1]
    catalogue_utile=[catalogue[-1]]

    #la liste est triée par puissance croissante
    for i in range (len(catalogue)-1):
        j=len(catalogue)-i-1 #on parcourt la liste à l'enver

        if catalogue[j-1][1]<catalogue_utile[0][1]: 
            catalogue_utile.insert(0,catalogue[j-1])
            prix_tmp=catalogue[j-1][1]
    
    filename_new="input/trucks_utile."+ str(x) + ".out"

    with open(filename_new, "w") as file :
        a=str(len(catalogue_utile))

        file.write(a+"\n")

        for  el in catalogue_utile :
            puissance = el[0]
            cout = el[1]

            file.write(str(puissance)+ " " + str(cout) + "\n")
            

c=[(1000,99),(2000, 294), (3000,365), (4000,382),(5000,295)]

print(catalogue_utile(0))


    
