#bubble sort 

n = [2,56,8,100,91,14]

for i in range (6):
    print ("PASS", i + 1 )
    print (n) 
    swap = False 
    for a in range (5):
        if n[a] > n[a+1]: 
            swap = True 
            b = n[a+1] 
            n[a+1] =n[a] 
            n[a] = b 
            print(n)
    if not swap:
        break 

            

#insertion sort 

for i in range (6):
    key = n[i]
    print ("KEY",key)
    print (n) 
    j = i-1 
    while j >=0 and key < n[j]:
        n[j+1] = n[j]
        j -=1
        print(n)
    n[j+1] = key 
    print (n)
    


