for a in range(11, 100):
        x = a
        for n in range(0,25):
            x = x + int(str(x)[::-1])
            if str(x) == str(x)[::-1]:
                if n > 20:
                    print(a, " ", x, "  ", n)                
                break 
       

       
              
            
                   
                