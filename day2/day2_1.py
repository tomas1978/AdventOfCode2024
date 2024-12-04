#day 2 problem 2, just started!
file = open("inputSmall.txt", "r")

content=1

def isIncreasing(list):
    for i in range(0,len(list)-1):
        if(list[i+1]<list[i]):
            return False
    return True

def isDecreasing(list):
    for i in range(0,len(list)-1):
        if(list[i+1]>list[i]):
            return False
    return True

while content:
    content=file.readline()
    numbers=content.split()
    if content:
        for i in range(0,len(numbers)):
            numbers[i]=int(numbers[i])    
        if isDecreasing(numbers):
            print("Decreasing")
        if isIncreasing(numbers):
            print("Decreasing")

        

