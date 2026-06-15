import numpy as np
import matplotlib.pyplot as plt

# ==========================
# CONSTANTES FÍSICAS
# ==========================

#T12 = 5730.0
#Lambda = np.log(2) / T12

Lambda = 1

N0 = 10**3

# ==========================
# CARGAR DATOS
# ==========================

microscopico = np.loadtxt("LÁTEX/TAREA2/microscopic.txt")
binomial = np.loadtxt("LÁTEX/TAREA2/binomial.txt")
poisson = np.loadtxt("LÁTEX/TAREA2/poisson.txt")

# Primera columna: tiempos
tiempos = microscopico[:, 0]

# Curva teórica
N_teorica = N0 * np.exp(-Lambda * tiempos)



# ==========================
# GRÁFICA
# ==========================



# --- Microscópico ---
for i in range(1, 4):
    plt.plot(
        tiempos,
        microscopico[:, i],
        color="blue",
        alpha=0.45,
        linewidth=1.5
    )

# --- Binomial ---
for i in range(1, 4):
    plt.plot(
        tiempos,
        binomial[:, i],
        color="green",
        alpha=0.45,
        linewidth=1.5
    )

# --- Poisson ---
for i in range(1, 4):
    plt.plot(
        tiempos,
        poisson[:, i],
        color="red",
        alpha=0.45,
        linewidth=1.5
    )

# --- Curva teórica ---
plt.plot(
    tiempos,
    N_teorica,
    color="black",
    linestyle="--",
    linewidth=2.5,
    label="Ley teórica"
)

# Para que la leyenda no repita 3 veces cada método
plt.plot([], [], color="blue", label="Microscópico")
plt.plot([], [], color="green", label="Binomial")
plt.plot([], [], color="red", label="Poisson")

plt.xlabel("TIEMPO (años)")
plt.ylabel("NÚCLEOS SUPERVIVIENTES")
plt.title("COMPARACIÓN DE MODELOS DE SIMULACIÓN")
plt.legend()
plt.savefig("LÁTEX/TAREA2/comparacion.png")

plt.show()