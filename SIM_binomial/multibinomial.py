import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.stats import binom, chisquare
from matplotlib.ticker import MultipleLocator

#### CONSTANTES FÍSICAS 
## Vamos a trabajar en años
#T12 = 5730.0
#Lambda = np.log(2)/T12

T12 = np.log(2)
Lambda = 1

n0 = 10**3 #número de núcleos a tiempo 0

t = 5 #tiempo que vamos a simular
dt = 0.1  #intervalo de tiempo
u = int(t/dt) #número de intervalos

N=n0 #número de núcleos supervivientes
D = 0 #número de núcleos desintegrados

p= 1- np.exp(-Lambda*dt) #probabilidad de desintegración en cada intervalo de tiempo

#Posición del tiempo de vida media en el array de supervivientes
pos_t12 = int(round( T12/dt))

inicio = time.perf_counter()




## FUNCIÓN DE SIMULACIÓN
def simulacion():
    supervivientes = []
    N=n0

    for i in range(u + 1):
        supervivientes.append(N)

        D = 0
        D = np.random.binomial(N, p)
        N -= D

    return supervivientes[pos_t12]       





# SIMULACIONES

num_simulaciones = 500

histograma = []
for i in range(num_simulaciones):
    Num = simulacion() 
    histograma.append(Num)

fin = time.perf_counter()

histograma = np.array(histograma)

media_exp = np.mean(histograma)
sigma_exp = np.std(histograma, ddof=1)



# GUARDAR DATOS
np.savetxt("SIM_binomial/500histograma.txt", histograma)




# GRAFICAMOS
plt.title("Núcleos supervivientes para la vida media de λ=1 en 500 simulaciones binomiales")




## HISTOGRAMA
# np.arrange no incluye el max, por eso sumamos 2 para incluirlo y restamos 0.5 para centrar las barras en los enteros.
plt.hist(
    histograma,
    bins=np.arange(min(histograma), max(histograma) + 2) - 0.5,
    edgecolor='black',
    alpha=0.7,
    label="Simulación"
)




# CALCULOS PARA CURVA TEÓRICA BINOMIAL
vidamedia_real = pos_t12 * dt

q = np.exp(-Lambda * vidamedia_real) #probabilidad de supervivencia a tiempo real, no el tiempo que usamos que es el valor entero más cercano a la vida media.

media_teorica = n0 * q
sigma_teorica = np.sqrt(n0 * q * (1 - q))

k = np.arange(min(histograma), max(histograma) + 1) 
#Lista de valores enteros desde el mínimo hasta el máximo número de núcleos supervivientes encontrados en las simulaciones, para calcular la frecuencia teórica de cada uno.

frecuencia_teorica = num_simulaciones * binom.pmf(k, n0, q)

## CURVA TEÓRICA BINOMIAL
plt.plot(
    k,
    frecuencia_teorica,
    "-", #dibuja un círculo en cada punto y los conecta con líneas
    label="Binomial teórica"
)




## LÍNEAS VERTICALES PARA MEDIA Y DESVIACIÓN ESTÁNDAR EXPERIMENTAL Y TEÓRICA


plt.axvline(media_exp, color="red", linestyle="-",
            label=f"Media exp = {media_exp:.2f}")

plt.axvline(media_exp + sigma_exp, color="green", linestyle="-",
            label=f"Media exp ± σ = {sigma_exp:.2f}")

plt.axvline(media_exp - sigma_exp, color="green", linestyle="-")

plt.axvline(media_teorica, color="blue", linestyle="-",
            label=f"Media teorica = {media_teorica:.2f}")  

plt.axvline(media_teorica + sigma_teorica, color="yellow", linestyle="-",
            label=f"Media teorica ± σ = {sigma_teorica:.2f}")

plt.axvline(media_teorica - sigma_teorica, color="yellow", linestyle="-")




# EJES Y CONFIGURACIÓN

plt.xlabel("NÚCLEOS SUPERVIVIENTES")
plt.ylabel("FRECUENCIA")
plt.legend()

ax = plt.gca()

ax.xaxis.set_major_locator(MultipleLocator(20))
ax.xaxis.set_minor_locator(MultipleLocator(10))

ax.yaxis.set_major_locator(MultipleLocator(3))
ax.yaxis.set_minor_locator(MultipleLocator(1))

plt.grid(True, which="major", alpha=0.3)
plt.grid(True, which="minor", alpha=0.1)
plt.savefig("SIM_binomial/500histograma.png")
plt.show()


## TEST CHI-CUADRADO

frecuencia_observada = []

for valor in k:
    frecuencia_observada.append(np.sum(histograma == valor))  #cuenta cuántas veces aparece cada valor en el histograma


frecuencia_esperada = num_simulaciones * binom.pmf(k, n0, q)

frecuencia_esperada = frecuencia_esperada * frecuencia_observada.sum() / frecuencia_esperada.sum()
#Multiplica toda la frecuencia esperada por un factor de corrección para que su suma total coincida con la suma observada

chi2, p_value = chisquare(
    f_obs=frecuencia_observada,
    f_exp=frecuencia_esperada
)




### IMPRIMIMOS POR PANTALLA LOS RESULTADOS ESTADÍSTICOS Y EL TIEMPO DE EJECUCIÓN

print("Media experimental:", media_exp)
print("Desviación estándar experimental:", sigma_exp)

print("Media teórica:", media_teorica)
print("Desviación estándar teórica:", sigma_teorica)

print("Chi-cuadrado:", chi2)
print("p-value:", p_value)

print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")