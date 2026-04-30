import matplotlib.pyplot as plt
import numpy as np

#### CONSTANTES FÍSICAS 
## Vamos a trabajar en años
T12 = 5730.0
Lambda = np.log(2)/T12

n0 = 10**2 #número de núcleos a tiempo 0

t = 10000 #tiempo que vamos a simular
dt = 150  #intervalo de tiempo
u = int(t/dt) #número de intervalos

N=n0 #número de núcleos supervivientes
D = 0 #número de núcleos desintegrados

p = Lambda*dt

def simulacion():
    tiempos = []
    supervivientes = []
    N=n0

    for i in range(u + 1):
        tiempos.append(i*dt)
        supervivientes.append(N)

        D = 0
        D = np.random.poisson(N*p)
        N -= D

    return tiempos, supervivientes        

# Ejecutar 3 simulaciones
tiempos, N1 = simulacion()
_, N2 = simulacion()
_, N3 = simulacion()

# Guardar todo junto
datos = np.column_stack((tiempos, N1, N2, N3))
np.savetxt("simulaciones/poisson.txt", datos)

tiempos = np.array(tiempos) #para graficar la solución exacta

# Graficar
plt.title("SIMULACIÓN POISSON")
plt.plot(tiempos, N1, label="Simulación 1")
plt.plot(tiempos, N2, label="Simulación 2")
plt.plot(tiempos, N3, label="Simulación 3")
plt.plot(tiempos, n0*np.exp(-Lambda*tiempos), label="Solución exacta")
plt.xlabel("TIEMPO (años)")
plt.ylabel("NÚCLEOS SUPERVIVIENTES")
plt.legend()
plt.savefig("simulaciones/poisson.png")
plt.show()