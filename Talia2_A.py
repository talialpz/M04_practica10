#Funció que treballa amb diversos factors del diccionari "myDict".
myDict = {'Talia':'Lopez', 'Edat':25, 'Pais':'Argentina', 'Capital':'Buenos Aires', 'Mida':1.57, 'Any':1997}

def func (**myDict):
    #Imprimeix la longitud del diccionari.
    print(len(myDict))
    #Imprimeix tots els valors del diccionari.
    print(myDict.values())
    #Extreu l'últim item del diccionari.
    print(myDict.popitem())
    print(myDict)

func(**myDict)




