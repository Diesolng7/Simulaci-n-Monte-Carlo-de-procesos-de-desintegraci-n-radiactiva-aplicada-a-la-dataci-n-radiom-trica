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
N0 = 50
lam = 0.4

# Tiempos elegidos en la binomial
tiempos = np.array([0.5, 1.5, 3.0, 5.0, 7.0])

# Valores centrales = valores medios
medias = N0 * np.exp(-lam * tiempos)

# Curva exponencial continua
t_cont = np.linspace(0, 7.5, 500)
N_teorica = N0 * np.exp(-lam * t_cont)

# -------------------------------
# Crear figura
# -------------------------------
plt.figure(figsize=(12, 7))

# Curva teórica
plt.plot(
    t_cont, N_teorica,
    linewidth=2,
    label=r'$N_0 e^{-\lambda t}$'
)

# Puntos correspondientes a los valores centrales
plt.scatter(
    tiempos, medias,
    s=80,
    zorder=5,
    label=r'Valores centrales de cada distribución binomial'
)

# Opcional: unir los puntos entre sí
plt.plot(tiempos, medias, linestyle='--', alpha=0.8)

# -------------------------------
# Etiquetas y título
# -------------------------------
plt.xlabel(r'$t\ (\mathrm{s})$')
plt.ylabel(r'Valor central, $\langle N(t)\rangle$')

plt.title(
    rf'EVOLUCIÓN TEMPORAL DEL VALOR CENTRAL DE $N(t)$' '\n'
    rf'($N_0={N0}$, $\lambda={lam}\,\mathrm{{s^{{-1}}}}$)'
)

# -------------------------------
# Ajustes finales
# -------------------------------
plt.xlim(0, 7.5)
plt.ylim(0, N0 + 2)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# Guardar figura
plt.savefig('valores_centrales_vs_tiempo.png', dpi=300, bbox_inches='tight')

# Mostrar
plt.show()