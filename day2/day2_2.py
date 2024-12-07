#day 2 problem 2, gives a too high result!
file = open("inputSmall.txt", "r")

content=1
numberOfSafeReports=0

#Global variable to indicate if one unsafe
#value has been removed
oneRemoved=False


def isIncreasing(list):
    removed=0
    for i in range(0,len(list)-1):
        if(list[i+1]<=list[i]):
            oneRemoved=True
            removed+=1
            if removed>1:
                return False
    return True

def isDecreasing(list):
    removed=0
    for i in range(0,len(list)-1):
        if(list[i+1]>=list[i]):
            oneRemoved=True
            removed+=1
            if removed>1:            
                return False
    return True

def isCorrectDistance(list):
    removed=0
    for i in range(0,len(list)-1):
        if(abs(list[i+1]-list[i])<1 or abs(list[i+1]-list[i])>3 ):
            removed+=1
            oneRemoved=True
            if removed>1:            
                return False
    return True

while content:
    content=file.readline()
    numbers=content.split()
    if content:
        for i in range(0,len(numbers)):
            numbers[i]=int(numbers[i])    
        oneRemoved=False
        if isDecreasing(numbers) and oneRemoved==True:
            oneRemoved=False
            if isCorrectDistance(numbers) and oneRemoved==False:
                numberOfSafeReports+=1
        oneRemoved=False
        if isDecreasing(numbers) and oneRemoved==False:
            oneRemoved=False
            if isCorrectDistance(numbers):
                numberOfSafeReports+=1
        oneRemoved=False
        if isIncreasing(numbers) and oneRemoved==True:
            oneRemoved=False
            if isCorrectDistance(numbers) and oneRemoved==False:
                numberOfSafeReports+=1
        oneRemoved=False
        if isIncreasing(numbers) and oneRemoved==False:
            oneRemoved=False
            if isCorrectDistance(numbers):
                numberOfSafeReports+=1


print("Number of safe reports: ",numberOfSafeReports)

        

