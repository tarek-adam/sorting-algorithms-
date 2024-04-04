class tri_rapide:
    @staticmethod
    def quicksort(liste):
        if len(liste) <= 1:
            return liste
        
        pivot = liste.pop()

        petit = []
        grand = []

        for nombre in liste:
            if nombre < pivot:
                petit.append(nombre)
            else:
                grand.append(nombre)
        
        return tri_rapide.quicksort(petit) + [pivot] + tri_rapide.quicksort(grand)

    @staticmethod
    def demander_liste_et_tri():
        print('Entrez une liste de nombres séparés par un espace:')
        input_list = input().split()  # Permet à l'utilisateur d'entrer une liste d'entiers séparés par des espaces
        input_list = [int(x) for x in input_list]  # Convertit les éléments de la liste en entiers

        sorted_list = tri_rapide.quicksort(input_list)  # Appelle la fonction quicksort avec la liste fournie par l'utilisateur
        print("Sorted list:", sorted_list)

tri_rapide.demander_liste_et_tri()
