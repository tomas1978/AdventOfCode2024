file = open("input.txt", "r")
list1=[]
list2=[]

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
    sum+=list1[i]+list2[i]    

print("Total sum: ",sum)
    
file.close()
