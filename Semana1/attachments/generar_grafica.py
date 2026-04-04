import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x + 3

x_line = np.linspace(-2, 12, 100)
y_line = f(x_line)

x_points = np.array([0, 1, 5, 10])
y_points = f(x_points)

plt.figure(figsize=(8, 5))
plt.plot(x_line, y_line, label='f(x) = 2x + 3', color='blue', zorder=1)
plt.scatter(x_points, y_points, color='red', label='Puntos calculados', zorder=2)

for xp, yp in zip(x_points, y_points):
    plt.annotate(f'({xp}, {yp:.0f})', (xp, yp), textcoords="offset points", xytext=(8, 8), fontsize=9)

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Función Lineal: f(x) = 2x + 3')
plt.legend()
plt.tight_layout()
plt.savefig('Semana1/attachments/funcion_lineal_2x3.png', dpi=150)
print('Imagen guardada en Semana1/attachments/funcion_lineal_2x3.png')
