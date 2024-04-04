class TriParPeigne:
    def __init__(self, arr):
        self.arr = arr
    
    def trier(self):
        arr = self.arr
        gap = len(arr)
        shrink = 1.3
        sorted = False
        
        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True
            
         
            i = 0
            while i + gap < len(arr):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]  # Swap
                    sorted = False
                i += 1
        
        return arr


if __name__ == "__main__":

    arr = [float(x) for x in input("Entrez une liste de nombres réels séparés par des espaces : ").split()]

    print("Entrée:", arr)
    
    tri_peigne = TriParPeigne(arr)
    resultat_trie = tri_peigne.trier()

    print("Résultat trié:", resultat_trie)
