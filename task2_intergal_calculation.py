import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа
num_points = 100000  # Кількість випадкових точок

# Генерація випадкових точок в прямокутній області
random_x = np.random.uniform(a, b, num_points)
random_y = np.random.uniform(0, max(f(random_x)), num_points)

# Підрахунок кількості точок, які попали під криву
points_under_curve = sum(random_y <= f(random_x))

# Обчислення площі прямокутної області та площі під кривою
rectangle_area = (b - a) * max(f(random_x))
area_under_curve = rectangle_area * (points_under_curve / num_points)

# Порівняння з точним значенням інтеграла
exact_value, error = quad(f, a, b)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()

if __name__ == '__main__':
    # Вивід результатів
    print("Значення інтегралу методом Монте-Карло:", area_under_curve)
    print("Точне значення інтегралу:", exact_value)
    plt.show()
