import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random 
from time import time
from ejercicio5 import insertsort
from ejercicio6 import quicksort

datos = [ii*100 for ii in range(1, 21)]
tiempo_is = []
tiempo_qs=[]

for ii in datos:
    lista_is = random.sample(range(0, 10000000), ii)
    lista_qs = lista_is.copy()

    t0 = time()
    insertsort(lista_is)
    tiempo_is.append(round(time()-t0, 6))

    t0 = time()
    quicksort(lista_qs)
    tiempo_qs.append(round(time()-t0, 6))

print("tiempos parciales de ejecucuion en inser sort {} [s]".format(tiempo_is))

print("tiempos parciales de ejecucuion en quick sort {} [s]".format(tiempo_qs))

fig, ax = plt.subplots("""111""")
ax.plot(datos, tiempo_is, label = "inser sort", marker = "*", color = "r")
ax.plot(datos, tiempo_qs, label = "quick sort", marker = "o", color = "b")

ax.set_xlabel("datos")
ax.set_ylabel("tiempo")
ax.grid(True)
ax.legend(loc=2)

plt.title("tiempos de ejecucion [s] insert sort vs quick sort")
plt.show()