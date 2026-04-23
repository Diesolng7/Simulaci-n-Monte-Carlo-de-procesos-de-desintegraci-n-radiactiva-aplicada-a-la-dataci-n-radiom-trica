import numpy as np
import matplotlib.pyplot as plt
from math import comb, exp

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
N0 = 50
lam = 0.4

# Tiempos
tiempos = [0.5, 1.5, 3.0, 5.0, 7.0]

# Valores posibles de N(t)
n_vals = np.arange(0, N0 + 1)

# -------------------------------
# Crear figura
# -------------------------------
plt.figure(figsize=(12, 7))

for t in tiempos:
    p_superv = exp(-lam * t)
    P = np.array([comb(N0, n) * (p_superv**n) * ((1 - p_superv)**(N0 - n)) for n in n_vals])
    
    media = N0 * p_superv
    
    line, = plt.plot(
        n_vals, P,
        marker='o',
        markersize=4,
        linestyle='-',
        linewidth=2,
        label=fr'$t={t}\,\mathrm{{s}}$'
    )
    
    color = line.get_color()
    plt.axvline(media, linestyle='--', color=color, alpha=0.8)

# -------------------------------
# Etiquetas y título
# -------------------------------
plt.xlabel(r'Número de núcleos no desintegrados, $N(t)$')
plt.ylabel(r'$P(N(t)=n)$')

plt.title(
    rf'DISTRIBUCIÓN BINOMIAL DE $N(t)$ PARA VARIOS TIEMPOS' '\n'
    rf'($N_0={N0}$, $\lambda={lam}\,\mathrm{{s^{{-1}}}}$)'
)

# -------------------------------
# Ajustes finales
# -------------------------------
plt.xlim(0, N0)
plt.ylim(bottom=0)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# Guardar figura
plt.savefig('distribucion_binomial_varios_tiempos.png', dpi=300, bbox_inches='tight')

# Mostrar
plt.show()