import matplotlib.pyplot as plt
import numpy as np
import time


#### CONSTANTES FÍSICAS 
## Vamos a trabajar en años
#T12 = 5730.0
#Lambda = np.log(2)/T12

Lambda = 1 

n0 = 10**2 #número de núcleos a tiempo 0

t = 5 #tiempo que vamos a simular
dt = 0.05  #intervalo de tiempo
u = int(t/dt) #número de intervalos

N = n0 #número de núcleos supervivientes
D = 0 #número de núcleos desintegrados

q= 1- np.exp(-Lambda*dt)

##Listas de resultados
tiempos = []
supervivientes = []

inicio = time.perf_counter()
## SIMULACION MICROSCÓPICA (núcleo a núcleo)
def simulacion():
    tiempos = []
    supervivientes = []
    
    N = n0
    interacciones = 0
    
    for j in range(u + 1):
        tiempos.append(j*dt)
        supervivientes.append(N)
        
        D = 0
        for i in range(N):
            interacciones += 1
            
            if np.random.random() < q:
                D += 1
                
        N -= D
    
    return tiempos, supervivientes, interacciones

# Ejecutar 3 simulaciones
tiempos, N1, interacciones1 = simulacion()
_, N2, interacciones2 = simulacion()
_, N3, interacciones3 = simulacion()

fin = time.perf_counter()

# Guardar todo junto
datos = np.column_stack((tiempos, N1, N2, N3))
np.savetxt("LÁTEX/TAREA2/TESTmicroscopic.txt", datos)



tiempos = np.array(tiempos) #para graficar la solución exacta

# Graficar
plt.title("SIMULACIÓN MICROSCÓPICA (Núcleo a núcleo)")
plt.plot(tiempos, N1, label="Simulación 1")
plt.plot(tiempos, N2, label="Simulación 2")
plt.plot(tiempos, N3, label="Simulación 3")
plt.plot(tiempos, n0*np.exp(-Lambda*tiempos), label="Solución exacta")
plt.xlabel("TIEMPO (años)")
plt.ylabel("NÚCLEOS SUPERVIVIENTES")
plt.legend()
plt.savefig("LÁTEX/TAREA2/TESTmicroscopic.png")
plt.show()


print("Tiempo de ejecución:", fin - inicio , "segundos")
print("Número de interacciones:", interacciones1 + interacciones2 + interacciones3)