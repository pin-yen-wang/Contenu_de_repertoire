import os

# Exercice 6.1 Contenu d'un répertoire

def scand(r):   
    f = []
    d = []
    for element in os.listdir(r):
        chemin = os.path.join(r, element)
        if os.path.isfile(chemin):
            f.append(element)
        elif os.path.isdir(chemin):
            d.append(element)
    return f, d
    


def main():
    r = 'C:\\Windows'  # ou un autre répertoire de votre choix
    # votre code de test ici...
    # Exemple
    # f, d = scand('C:\Windows')
    # print(f)
    # print(d)
    pass

if __name__ == '__main__':
    main()