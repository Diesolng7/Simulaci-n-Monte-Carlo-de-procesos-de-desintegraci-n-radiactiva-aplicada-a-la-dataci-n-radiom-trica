import numpy as np
import matplotlib.pyplot as plt

# Personalización
plt.rcParams.update({
    'font.size': 22,          # tamaño general
    'axes.titlesize': 20,     # título
    'axes.labelsize': 18,     # ejes
    'xtick.labelsize': 18,    # números eje x
    'ytick.labelsize': 18,    # números eje y
    'legend.fontsize': 18     # leyenda
})

# Variable tiempo
t = np.linspace(0, 5, 1000)

# Valores de lambda
lambdas = [0.5, 1, 2]

# Crear figura
plt.figure(figsize=(8, 5))

# Dibujar densidades y sus ⟨t⟩
for lam in lambdas:
    f = lam * np.exp(-lam * t)
    
    # Dibujar curva y guardar color
    line, = plt.plot(t, f, label=fr'$\lambda={lam}$')
    
    # Color de la curva
    color = line.get_color()
    
    # Vida media ⟨t⟩
    t_mean = 1 / lam
    
    # Línea discontinua del mismo color
    plt.axvline(t_mean, linestyle='--', color=color,
                label=fr'$\langle t \rangle={t_mean:.2f}$')

# Etiquetas
plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()

# Guardar
plt.savefig('LÁTEX/Gráficas/f(t).jpg', dpi=300, bbox_inches='tight')



# Mostrar
plt.show()