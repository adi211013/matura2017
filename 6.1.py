file=open("dane.txt","r")
pixels=[]
for line in file:
    xd=line.split()
    for l in xd:
        pixels.append(int(l))
file.close()


brightest=max(pixels)
darkest=min(pixels)
print(brightest,darkest)
#print(pixels)