list2 = [2,5,7,9,10,123,456,777,988]

ask2 = int(input("Enter value you would like to search:"))

low = 0 
high = 8 
flag = False 
while low <= high: 
    medium = (low + high)//2 

    if list2 [medium] == ask2: 
        print ("Key Found")
        flag = True 
        break 
    elif list2 [medium] > ask2:
        high = medium - 1 

    elif list2 [medium] < ask2:
        low = medium + 1 
if flag == False:
    print("Key doesn't exist")


