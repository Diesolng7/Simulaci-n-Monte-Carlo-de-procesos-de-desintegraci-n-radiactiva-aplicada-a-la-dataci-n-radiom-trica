import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#########################################################
################ PARÁMETROS GENERALES ##################
#########################################################

Lambda = 1.0
N0 = 1000

carpeta_salida = Path("LÁTEX/TAREA2")


#########################################################
################ CARGAR DATOS ##########################
#########################################################

# OJO: usa el nombre real de tu archivo.
# Si tu archivo se llama "microscopic.txt", cambia "microscopico.txt" por "microscopic.txt".
microscopico = np.loadtxt(carpeta_salida / "microscopic.txt")
binomial = np.loadtxt(carpeta_salida / "binomial.txt")
poisson = np.loadtxt(carpeta_salida / "poisson.txt")

# Primera columna: tiempos
tiempos = microscopico[:, 0]

# Ley teórica
N_teorica = N0 * np.exp(-Lambda * tiempos)


#########################################################
############### FORMATO COMÚN DE GRÁFICAS ##############
#########################################################

plt.rcParams.update({
    "font.size": 13,
    "axes.titlesize": 15,
    "axes.labelsize": 13,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "legend.fontsize": 10,
    "figure.figsize": (7.2, 4.8),
    "axes.grid": False,
    "lines.linewidth": 1.8
})


#########################################################
################ GRÁFICA COMPARATIVA ###################
#########################################################

plt.figure()

# Modelo microscópico: 3 curvas azules
for i in range(1, 4):
    plt.plot(
        tiempos,
        microscopico[:, i],
        color="blue",
        alpha=0.45,
        linewidth=1.5,
        label="Microscópic" if i == 1 else None
    )

# Modelo binomial: 3 curvas verdes
for i in range(1, 4):
    plt.plot(
        tiempos,
        binomial[:, i],
        color="green",
        alpha=0.45,
        linewidth=1.5,
        label="Binomial" if i == 1 else None
    )

# Modelo de Poisson: 3 curvas rojas
for i in range(1, 4):
    plt.plot(
        tiempos,
        poisson[:, i],
        color="red",
        alpha=0.45,
        linewidth=1.5,
        label="Poisson" if i == 1 else None
    )

# Ley teórica
plt.plot(
    tiempos,
    N_teorica,
    color="black",
    linestyle="--",
    linewidth=2.3,
    label="Ley teórica"
)


plt.xlabel("t (años)")
plt.ylabel(r"$N_s(t)$")
plt.xlim(0, tiempos[-1])
plt.ylim(0, N0 * 1.05)
plt.legend(loc="upper right")
plt.tight_layout()

plt.savefig(carpeta_salida / "comparacion.png", dpi=300, bbox_inches="tight")
plt.show()