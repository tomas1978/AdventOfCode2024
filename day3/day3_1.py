#day 3 problem 1, 11 dec 
#12 dec creating a list with positions of all mul instructions
#13 dec starting to find ( , )
#14 dec trying a new approach

file = open("inputSmall.txt", "r")
data=file.readline()
mulPositions=[]
lastMul=0
while lastMul!=-1:
    print(lastMul)
    lastMul=data.find("mul", lastMul+1, len(data))
    if lastMul!=-1:
        mulPositions.append(lastMul)
#print(mulPositions)

#Does not work at all, must probably be re-written from scratch
for i in range(0,len(mulPositions)-6):
    if i<len(mulPositions):
        for j in range(mulPositions[i], mulPositions[i+1]):
            if mulPositions[j-1]=='(':
                leftParenthesis=j
                print(leftParenthesis)

    