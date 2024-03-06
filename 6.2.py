file=open("dane.txt","r")
pixels=[]
for line in file:
    xd=line.split()
    pixels.append(xd)
file.close()
badlines=[]
#print(pixels)
for i in range(0,200):
    for j in range(0,319):
         if pixels[i][j]!=pixels[i][319-j]:
            badlines.append(i)
            break;

#print(len(pixels))
print(len(badlines))
