pixels=[]
file=open("dane.txt","r")
for line in file:
    xd=line.split()
    pixels.append(xd)
file.close()
max=0
for j in range(0,320):
    temp=1
    for i in range(0,199):
        if pixels[i][j]==pixels[i+1][j]:
          temp+=1
        else:
            if temp > max:
                max = temp
            temp=1
    if temp>max:
        max=temp
print(max)