

def reverse_number (n): 
    if n <= 1: 
        print(n)
    else: 
       print (n%10) 
       return reverse_number (n//10)

       
        
    

reverse_number (12345)
    
    