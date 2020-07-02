li = [["Darcy",1], ["Sophie",2],["Ife",3]]

f = open("namesAndScores.txt" , "w")
for i in range(0, len(li)):
    f.write(li[i][0])
    f.write(",")
    f.write(str(li[i][1]))
    f.write("\n")
f.close()

f = open("namesAndScores.txt",'r' )
txt = f.readlines()
for i in range(0,len(txt)):
    txt[i]=txt[i].strip("\n")
    txt[i]=txt[i].split(",")
    txt[i][1]= int(txt[i][1])
print(txt)
f. close()
