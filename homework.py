n = [0,1,2,3,4,5,6,7,8,9,10]
low = 0 
high = 10 
ask = int(input("Please enter the value you would like to search: "))
def calcmedium(n,low,high,ask):
    medium = (low+high)//2 
    if low <= high: 
        if n[medium] == ask:
            return medium 
        elif n[medium] < ask:
            return calcmedium (n, medium +1, high, ask)
        else: 
            return calcmedium (n,low, medium - 1, ask)
    else: 
        return ("Value is not found ")

print(calcmedium (n,low,high,ask))


