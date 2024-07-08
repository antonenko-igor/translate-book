#Program written by Antonenko Igor
words = [line.strip() for line in open('wordlist.txt')]
Z = []
for word in words:
    if len(word) == 8:
        Z.append(word)
for word_start in Z:
    A = []
    A.append(word_start)
    B = A[:]
    while True:
        C = []
        for word in B:
            for i in range(len(word)):
                if word[:(0 + i)] + word[(1+i):]  in words:
                     C.append( word[:(0 + i)] + word[(1+i):])
        C = list(set(C))
        if len(C) != 0:
            B = C[:]
            A += C
        else:
            break
        s = "".join(A[-1:])
        if len(s) == 1:
            print(A) 

    
        
    
                    

    
    
        
            
               
    
    
        




   
       

        














        

         

                    


















  
    
    



        

    
        
            

        




   
