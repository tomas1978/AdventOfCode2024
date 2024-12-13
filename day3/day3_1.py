#day 3 problem 1, 11 dec just started
#12 dec creating a list with positions of all mul instructions
file = open("inputSmall.txt", "r")
data=file.readline()
mulPositions=[]
lastMul=0
while lastMul!=-1:
    print(lastMul)
    lastMul=data.find("mul", lastMul+1, len(data))
    if lastMul!=-1:
        mulPositions.append(lastMul)
print(mulPositions)

for i in range(0,len(mulPositions)):
    leftParanthesis=data.find("(",mulPositions[i])
    comma=data.find(",")
    rightParanthesis=data.find(")",mulPositions[i])
    print("left: ",leftParanthesis, "comma", comma, "right",rightParanthesis)

    