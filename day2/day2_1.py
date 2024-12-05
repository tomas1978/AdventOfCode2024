#day 2 problem 2, solved!
file = open("input.txt", "r")

content=1
numberOfSafeReports=0

def isIncreasing(list):
    for i in range(0,len(list)-1):
        if(list[i+1]<=list[i]):
            return False
    return True

def isDecreasing(list):
    for i in range(0,len(list)-1):
        if(list[i+1]>=list[i]):
            return False
    return True

def isCorrectDistance(list):
    for i in range(0,len(list)-1):
        if(abs(list[i+1]-list[i])<1 or abs(list[i+1]-list[i])>3 ):
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

        

