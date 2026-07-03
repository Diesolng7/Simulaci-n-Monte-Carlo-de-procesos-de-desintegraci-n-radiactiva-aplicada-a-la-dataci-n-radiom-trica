import numpy as np
import matplotlib.pyplot as plt

# Personalización
plt.rcParams.update({
    'font.size': 18,
    'axes.titlesize': 16,
    'axes.labelsize': 18,
    'xtick.labelsize': 18,
    'ytick.labelsize': 18,
    'legend.fontsize': 18
})

# Variable Δt
dt = np.linspace(0, 3, 1000)

# Parámetro lambda
lam = 1.0

# Probabilidades
p_exacta = 1 - np.exp(-lam * dt)
p_aprox = lam * dt

# Punto donde deja de ser buena aproximación
dt_lim = 0.1 / lam
p_lim = lam * dt_lim

# Crear figura
plt.figure(figsize=(8, 5))

# Curvas
plt.plot(dt, p_exacta, label=r'$q(\Delta t) = 1 - e^{-\lambda \Delta t}$')
plt.plot(dt, p_aprox, '--', label=r'$q(\Delta t) = \lambda \Delta t$')
plt.ylabel(r'$q(\Delta t)$')

# Punto crítico
plt.scatter(dt_lim, p_lim, zorder=5)
plt.axvline(dt_lim, linestyle=':', color='gray')
plt.axhline(p_lim, linestyle=':', color='gray')

# Texto del punto
plt.text(dt_lim*1.05, p_lim*0.9,
         r'$\lambda \Delta t \approx 0.1$',
         fontsize=16)


# Etiquetas
plt.xlabel(r'$\Delta t\ (\mathrm{s})$')
plt.ylabel(r'$q(\Delta t)$')


plt.xlim(0, 0.25)
plt.ylim(0, 0.25)
plt.legend()

# Guardar
plt.savefig('LÁTEX/Gráficas/exacta_vs_aprox.jpg', dpi=300, bbox_inches='tight')

# Mostrar
plt.show()