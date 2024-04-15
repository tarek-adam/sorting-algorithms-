class tri_par_insertion:
    def tri_par_insertion (l):
        for i in range (1, len(l)):
            cle = l[i]
            
            j = i-1
            while j >= 0 and cle < l[j]:
                 l[j+1] = l[j]
                 j -= 1
            l[j+1] = cle
                 
l = [5,3,8,6,9,10,-5,3,4,8,2]
tri = tri_par_insertion
tri.tri_par_insertion(l)
print(l)

