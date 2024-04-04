class tri_par_tas: 
    @staticmethod
    def tri_par_tas(arr):
        # Créer un tas max
        def creer_tas(arr):
            n = len(arr)
            # Commence par l'indice du dernier parent
            start = (n // 2) - 1

            # Construire un tas à partir du bas
            for i in range(start, -1, -1):
                entasser(arr, n, i)

        # Fonction pour entasser un nœud i
        def entasser(arr, n, i):
            largest = i  # Initialiser le plus grand comme racine
            left = 2 * i + 1  # indice du fils gauche
            right = 2 * i + 2  # indice du fils droit

            # Vérifier si le fils gauche existe et est plus grand que la racine
            if left < n and arr[left] > arr[largest]:
                largest = left

            # Vérifier si le fils droit existe et est plus grand que la racine
            if right < n and arr[right] > arr[largest]:
                largest = right

            # Changer la racine si nécessaire
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # swap
                # Entasser le sous-arbre affecté récursivement
                entasser(arr, n, largest)

        # Tri par tas
        def trier(arr):
            n = len(arr)
            # Construire un tas
            creer_tas(arr)
            # Extraire des éléments un par un du tas
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]  # swap
                entasser(arr, i, 0)

        trier(arr)


    if __name__ == "__main__":

        arr = [int(x) for x in input("Entrez une liste de nombres réels séparés par des espaces : ").split()]
        
        print("Entrée:", arr)
        
        tri_par_tas(arr)
        
        print("Résultat trié:", arr)
