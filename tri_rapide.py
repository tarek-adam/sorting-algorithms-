def quicksort(liste):
    if len(liste) <=1:
        return liste
    
    pivot = liste.pop()


    petit = []
    grand = []

    for nombre in liste:
        if nombre < pivot:
            petit.append(nombre)

        else:
            grand.append(nombre)
    
    return quicksort(petit)+[pivot]+quicksort(grand)

def demander_liste_et_tri():
    print('Entrez une liste de nombres séparés par un espace:')
    input_list = input().split()  # Permet à l'utilisateur d'entrer une liste d'entiers séparés par des espaces
    input_list = [int(x) for x in input_list]  # Convertit les éléments de la liste en entiers

    sorted_list = quicksort(input_list)  # Appelle la fonction quicksort avec la liste fournie par l'utilisateur
    print("Sorted list:", sorted_list)

demander_liste_et_tri() 