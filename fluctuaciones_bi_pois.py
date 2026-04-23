import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Personalización visual
# -------------------------------
plt.rcParams.update({
    'font.size': 18,
    'axes.titlesize': 20,
    'axes.labelsize': 18,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 14
})

# -------------------------------
# Parámetros físicos
# -------------------------------
N0 = 50          # número inicial de núcleos
lam = 0.4        # constante de desintegración (s^-1)
n_realizaciones = 12

# Mallado temporal
t = np.linspace(0, 7.0, 300)

# Probabilidad de supervivencia en cada instante
p_superv = np.exp(-lam * t)

# -------------------------------
# Simulaciones Monte Carlo
# -------------------------------
# En cada tiempo, N(t) ~ Bin(N0, e^{-lambda t})
trayectorias = np.array([
    np.random.binomial(N0, p_superv) for _ in range(n_realizaciones)
])

# Valor medio teórico
N_media = N0 * np.exp(-lam * t)

# Desviación típica teórica
sigma = np.sqrt(N0 * p_superv * (1 - p_superv))

# -------------------------------
# Crear figura
# -------------------------------
plt.figure(figsize=(12, 7))

# Banda de fluctuación ± sigma
plt.fill_between(
    t, N_media - sigma, N_media + sigma,
    alpha=0.25,
    label=r'Banda $\langle N(t)\rangle \pm \sigma_{N(t)}$'
)

# Trayectorias simuladas
for i in range(n_realizaciones):
    plt.step(
        t, trayectorias[i],
        where='post',
        linewidth=1.5,
        alpha=0.75
    )

# Curva media
plt.plot(
    t, N_media,
    linewidth=3,
    label=r'Valor medio $\langle N(t)\rangle = N_0 e^{-\lambda t}$'
)

# -------------------------------
# Etiquetas y título
# -------------------------------
plt.xlabel(r'$t\ (\mathrm{s})$')
plt.ylabel(r'Número de núcleos no desintegrados, $N(t)$')

plt.title(
    rf'FLUCTUACIONES ESTADÍSTICAS DEL NÚMERO DE SUPERVIVIENTES $N(t)$' '\n'
    rf'($N_0={N0}$, $\lambda={lam}\,\mathrm{{s^{{-1}}}}$)'
)

# -------------------------------
# Ajustes finales
# -------------------------------
plt.xlim(0, 7.0)
plt.ylim(0, N0 + 2)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# Guardar figura
plt.savefig('fluctuaciones_Nt.png', dpi=300, bbox_inches='tight')

# Mostrar
plt.show()