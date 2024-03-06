import math
kontrastCounter=0
pixels=[]
file=open("dane.txt","r")
for line in file:
    xd=line.split()
    pixels.append(xd)
file.close()
for i in range(0,200):
    for j in range(0,320):
        if i-1<0 or i+1>199 or j+1>319 or j-1<0:
            continue
        if math.fabs(int(pixels[i][j]) - int(pixels[i - 1][j])) > 128:
            kontrastCounter += 1
        elif math.fabs(int(pixels[i][j]) - int(pixels[i + 1][j])) > 128:
            kontrastCounter += 1
        elif math.fabs(int(pixels[i][j]) - int(pixels[i][j-1])) > 128:
            kontrastCounter += 1
        elif math.fabs(int(pixels[i][j]) - int(pixels[i][j+1])) > 128:
            kontrastCounter += 1

print(kontrastCounter)