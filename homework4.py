n = [64,34,25,12,22,11,90]

for i in range (7):
    print ("PASS", i+1)
    print (n)
    swap = False 
    for a in range (6):
        if n[a] < n[a+1]: 
            swap = True 
            b = n[a+1] 
            n[a+1] =n[a] 
            n[a] = b 
            print(n)
    if not swap:
        break 