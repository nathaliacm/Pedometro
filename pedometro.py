import os
import json
import matplotlib.pyplot as plt

path = "C:\\Users\\natha\\workspace\\pedometro\\em frente com paradas"
files = os.listdir(path)

accelerations = None
rotations = None

for file in files:
    if(".json" in file):
        if(file[:-5] == "accelerations"):
            with open(path + "/" + file) as data_file:
                accelerations = json.load(data_file)
        if(file[:-5] == "rotations"):
            with open(path + "/" + file) as data_file:
                rotations = json.load(data_file)

NS2S = 1.0 / 1000000.0

#Salvar x y z 
x = []
y = []
z = []
time_usec = []

dt = []

x_g = []
y_g = []
z_g = []
w =[]
time = []

saltos = 0
passos = 0

for axis in accelerations["accelerations"]:
    x.append(round(axis["x"],2))
    y.append(round(axis["y"],2))
    z.append(round(axis["z"],2))
    time_usec.append(axis["time_usec"])

for axis in rotations["rotations"]:
    x_g.append(round(axis["x"],2))
    y_g.append(round(axis["y"],2))
    z_g.append(round(axis["z"],2))
    

for i in range(len(y)-1):
    dt.append((time_usec[i+1] - time_usec[i])*NS2S)
    time.append((time_usec[i+1] - time_usec[i])*NS2S)
    w.append(y_g[i])
    if y[i]>12:
        saltos +=1
    elif y[i]<12 and saltos != 0:
        print("tempo: ",round(sum(time),2),"sec | 1 passo | v angular = ",sum(w))
        w = []
        dt = []
        passos += 1
        saltos = 0
    if sum(dt)>1:
        print("parado")
        dt = []

print("\n",passos,"passos")    
plt.plot(y)


plt.show()
