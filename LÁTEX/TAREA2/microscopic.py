import numpy as np
import matplotlib.pyplot as plt
import time
from pathlib import Path

#########################################################
################ PARÁMETROS GENERALES ##################
#########################################################

# Constantes de la simulación
Lambda = 1.0                 # año^{-1}
N0 = 1000                    # núcleos iniciales
T_sim = 5.0                  # años
dt = 0.05                    # años

# Número de pasos temporales
n_pasos = int(round(T_sim / dt))

# Vector temporal
tiempos = np.linspace(0, T_sim, n_pasos + 1)

# Probabilidades en un paso temporal
p_supervivencia = np.exp(-Lambda * dt)
q = 1.0 - p_supervivencia

# Generador aleatorio
rng = np.random.default_rng(12345)

# Carpeta de salida
carpeta_salida = Path("LÁTEX/TAREA2")
carpeta_salida.mkdir(parents=True, exist_ok=True)


#########################################################
############### FORMATO COMÚN DE GRÁFICAS ##############
#########################################################

plt.rcParams.update({
    "font.size": 13,
    "axes.titlesize": 16,
    "axes.labelsize": 14,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "legend.fontsize": 14,
    "figure.figsize": (7.2, 4.8),
    "axes.grid": False,
    "lines.linewidth": 1.8
})


def guardar_grafica(tiempos, simulaciones, nombre_archivo, titulo):
    """
    Representa tres simulaciones junto con la ley exponencial teórica
    usando un formato común para todas las figuras del apartado.
    """

    plt.figure()

    for i, N in enumerate(simulaciones, start=1):
        plt.plot(tiempos, N, label=f"Simulación {i}")

    plt.plot(
        tiempos,
        N0 * np.exp(-Lambda * tiempos),
        linestyle="--",
        color="black",
        label="Ley teórica"
    )

   
    plt.xlabel("t (años)")
    plt.ylabel(r"$N_s(t)$")
    plt.xlim(0, T_sim)
    plt.ylim(0, N0 * 1.05)
    plt.legend()
    plt.tight_layout()

    plt.savefig(carpeta_salida / nombre_archivo, dpi=300, bbox_inches="tight")
    plt.show()


#########################################################
############### MODELO A: NÚCLEO A NÚCLEO ##############
#########################################################

def simulacion_nucleo_a_nucleo():
    supervivientes = []
    N = N0

    for _ in tiempos:
        supervivientes.append(N)

        # Se genera un número aleatorio por cada núcleo superviviente
        numeros_aleatorios = rng.random(N)

        # Núcleos desintegrados en el intervalo
        D = np.sum(numeros_aleatorios < q)

        # Actualización de núcleos supervivientes
        N -= D

    return np.array(supervivientes)


#########################################################
################ EJECUCIÓN DE SIMULACIONES #############
#########################################################

inicio = time.perf_counter()

N1 = simulacion_nucleo_a_nucleo()
N2 = simulacion_nucleo_a_nucleo()
N3 = simulacion_nucleo_a_nucleo()

fin = time.perf_counter()


#########################################################
################ GUARDAR DATOS Y FIGURA ################
#########################################################

datos = np.column_stack((tiempos, N1, N2, N3))
np.savetxt(carpeta_salida / "microscopico.txt", datos)

guardar_grafica(
    tiempos,
    [N1, N2, N3],
    "microscopic.png",
    "Modelo A: núcleo a núcleo"
)


#########################################################
################ COSTE COMPUTACIONAL ###################
#########################################################

coste_aproximado = np.sum(N1) + np.sum(N2) + np.sum(N3)

print("Coste aproximado:", coste_aproximado)
print("Tiempo de ejecución:", fin - inicio, "segundos")