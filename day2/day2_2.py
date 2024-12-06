#day 2 problem 2, gives a too high result!
file = open("input.txt", "r")

content=1
numberOfSafeReports=0


def isIncreasing(list):
    removed=0
    for i in range(0,len(list)-1):
        if(list[i+1]<=list[i]):
            removed+=1
            if removed>1:
                return False
    return True

def isDecreasing(list):
    removed=0
    for i in range(0,len(list)-1):
        if(list[i+1]>=list[i]):
            removed+=1
            if removed>1:            
                return False
    return True

def isCorrectDistance(list):
    removed=0
    for i in range(0,len(list)-1):
        if(abs(list[i+1]-list[i])<1 or abs(list[i+1]-list[i])>3 ):
            removed+=1
            if removed>1:            
                return False
    return True

while content:
    content=file.readline()
    numbers=content.split()
    if content:
        for i in range(0,len(numbers)):
            numbers[i]=int(numbers[i])    
        if((isDecreasing(numbers) or isIncreasing(numbers)) and isCorrectDistance(numbers)):
            numberOfSafeReports+=1

print("Number of safe reports: ",numberOfSafeReports)

        

