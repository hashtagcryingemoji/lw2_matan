import numpy as np
import matplotlib.pyplot as plt

v0 = 2.97  # м/с
angle = 46.6  # градусы
g = 10  # м/с²

angle_rad = np.radians(angle)
sin_val = np.sin(angle_rad)

t_max = 2 * v0 * sin_val / g
t = np.linspace(0, t_max, 200)
y = v0 * sin_val * t - 0.5 * g * t**2

plt.figure(figsize=(10, 6))
plt.plot(t, y, 'b-', linewidth=3)
plt.xlabel('Время (секунды)', fontsize=12)
plt.ylabel('Высота (метры)', fontsize=12)
plt.title(f'Бросок под углом {angle}° со скоростью {v0} м/с', fontsize=14)
plt.grid(True, alpha=0.3)

t_max_h = v0 * sin_val / g
y_max = v0 * sin_val * t_max_h - 0.5 * g * t_max_h**2

plt.plot(0, 0, 'go', markersize=10, label='Старт')
plt.plot(t_max_h, y_max, 'ro', markersize=10, label=f'Макс: {y_max:.3f} м')
plt.plot(t_max, 0, 'mo', markersize=10, label=f'Падение: {t_max:.3f} с')

plt.legend(loc='upper right')
plt.xlim(0, t_max * 1.05)
plt.ylim(0, y_max * 1.1)

plt.tight_layout()
plt.savefig('simple_trajectory.png', dpi=300)
plt.show()
