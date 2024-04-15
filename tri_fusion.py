class tri_fusion:
    def tri_fusion(l):
        if len(l) > 1:
           m = len(l) // 2
        
           g = l[m:]
           d = l[:m]
        
           tri_fusion.tri_fusion(g) # [1,4]
           tri_fusion.tri_fusion(d) # [2,3,5]
        
           i, j, k = 0, 0, 0
           while i < len(g) and j < len(d): # [...] [...]
               if g[i] < d[j]:
                  l[k] = g[i]
                  i += 1
               else:
                   l[k] = d[j]
                   j += 1
               k += 1
            
           while i < len(g): # [...] []
               l[k] = g[i]
               i += 1
               k += 1
            
           while j < len(d): # [] [...]
               l[k] = d[j]
               j += 1
               k += 1
  
l = [1,4,3,5,2]
tri = tri_fusion()
tri_fusion.tri_fusion(l)
print(l)          
            
        