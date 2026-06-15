import matplotlib.pyplot as plt
import numpy as np
import time



#### CONSTANTES FÍSICAS 
## Vamos a trabajar en años
# T12 = 5730.0
# Lambda = np.log(2)/T12

T12 = np.log(2)
Lambda = np.log(2) / T12

n0 = 10**3  # número de núcleos a tiempo 0

t = 5       # tiempo total que vamos a simular
dt = 0.1    # intervalo de tiempo
u = int(t/dt)  # número de intervalos
tiempos = np.arange(u + 1) * dt

N_teorico = n0 * np.exp(-Lambda * tiempos)


# Posición del tiempo de vida media
pos_t12 = int(round(T12 / dt))

num_simulaciones = 50



inicio = time.perf_counter()

# Hay un problema en esta simulación y es que no vale para hacer trayectorias ya que al utilizar la fórmula de la binomial cada vez que amuentamos el tiempo, el número de núcleos cambia pero al no considerar el número de núcleos del step anterior, pueden salir más núcleos de los que hay en el anterior step(no tiene sentido), por ello he cambiado esto

#for i in range(num_simulaciones):
#    for j in range(u + 1):
#        N = np.random.binomial(n0, np.exp(-Lambda * j * dt))
#        M[i][j] = N


M = np.zeros((num_simulaciones, u + 1))

q_step = np.exp(-Lambda * dt)

for i in range(num_simulaciones):
    N = n0
    M[i, 0] = N

    for j in range(1, u + 1):
        N = np.random.binomial(N, q_step)
        M[i, j] = N

fin = time.perf_counter()

media_exp = np.mean(M, axis=0)
desviacion_exp = np.std(M, axis=0, ddof=1)



np.savetxt("Matriz_binomial_500sim_1000nucleos.txt", M)

print(f"Tiempo de ejecución: {fin - inicio} segundos")



##########################################
############ PRIMERA GRÁFICA ############
#########################################

trayectorias = [0, 1, 2, 3]

plt.figure(figsize=(8, 5))

# Trayectorias individuales
for i in trayectorias:
    plt.plot(tiempos, M[i, :], label=f"Trayectoria {i+1}")

# Media experimental con desviación estándar
plt.errorbar(
    tiempos,
    media_exp,
    yerr=desviacion_exp,
    fmt="o",
    markersize=3,
    capsize=2,
    label=r"$\bar{N}_i \pm \sigma_i$"
)

# Curva teórica
plt.plot(
    tiempos,
    N_teorico,
    linewidth=2.5,
    label=r"$N(t)=N_0e^{-\lambda t}$"
)

plt.xlabel("Tiempo")
plt.ylabel("Núcleos supervivientes")
plt.title("Trayectorias, media simulada y ley teórica")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figura1_trayectorias.png", dpi=300)
plt.show()




##########################################
############ SEGUNDA GRÁFICA ############
##########################################

valores_M = [5, 10, 50, 100, 500, 1000]
errores_delta = []

for M_sim in valores_M:

    matriz = np.zeros((M_sim, u + 1))

    for i in range(M_sim):
        N = n0
        matriz[i, 0] = N

        for j in range(1, u + 1):
            N = np.random.binomial(N, q_step)
            matriz[i, j] = N

    media_t12 = np.mean(matriz[:, pos_t12])

    teorico_t12 = n0 * np.exp(-Lambda * tiempos[pos_t12])

    Delta = abs(media_t12 - teorico_t12) / teorico_t12

    errores_delta.append(Delta)


plt.figure(figsize=(8, 5))

plt.plot(
    valores_M,
    errores_delta,
    "o-",
    label=r"$\Delta$ en $t=T_{1/2}$"
)

plt.xscale("log")

plt.xlabel("Número de simulaciones M")
plt.ylabel(r"$\Delta$")
plt.title(r"Convergencia de $\bar{N}$ hacia $N(t)$ en $t=T_{1/2}$")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("figura2_convergencia_t12.png", dpi=300)
plt.show()