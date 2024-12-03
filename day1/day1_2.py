#day 1 problem 2, solved!
file = open("input.txt", "r")
list1=[]
list2=[]
similarityScore=0

#Counts how many times value appears in list
def countAppearances(list, value):
    appearances=0
    for i in range(0, len(list)):
        if(list[i]==value):
            appearances+=1
    return appearances

while True:
    content=file.readline()
    if not content:
        break
    values=content.split()
    list1.append(int(values[0]))
    list2.append(int(values[1]))

list1.sort()
list2.sort()
sum=0

for i in range(0,len(list1)):
    similarityScore+=countAppearances(list2,list1[i])*list1[i]  

print("Total similarity score: ",similarityScore)
    
file.close()
