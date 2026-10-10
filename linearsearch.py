list1 = [2,456,7,10,9,123,5,777,988]

ask = int (input("Enter a number you would like to search:"))

for i in range(len(list1)):
    if ask == list1[i]:
        print ("Key Found")
        break 
    else:
        print ("Key doesn't exist")
    break
