import numpy as np
import matplotlib.pyplot as plt

# ==========================
# CONSTANTES FÍSICAS
# ==========================

T12 = 5730.0
Lambda = np.log(2) / T12

N0 = 1000

# ==========================
# CARGAR DATOS
# ==========================

microscopico = np.loadtxt("simulaciones/microscopic.txt")
binomial = np.loadtxt("simulaciones/binomial.txt")
poisson = np.loadtxt("simulaciones/poisson.txt")

# Primera columna: tiempos
tiempos = microscopico[:, 0]

# Curva teórica
N_teorica = N0 * np.exp(-Lambda * tiempos)

# ==========================
# GRÁFICA
# ==========================

plt.figure(figsize=(10, 6))

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

plt.xlabel("Tiempo (años)")
plt.ylabel("Núcleos supervivientes")
plt.title("Comparación entre simulaciones")
plt.legend()
plt.grid(True)
plt.savefig("simulaciones/comparacion.png")

plt.show()