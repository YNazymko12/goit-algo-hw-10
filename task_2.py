import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції та межі інтегрування
def f(x):
    return x**2

a = 0  # Нижня межа інтегрування
b = 2  # Верхня межа інтегрування

# Функція для обчислення інтегралу методом Монте-Карло
def monte_carlo(f, a, b, num_samples=10000):
    # Генерація випадкових точок в інтервалі [a, b]
    random_x = np.random.uniform(a, b, num_samples)
    # Обчислення значень функції в цих точках
    random_y = f(random_x)
    # Обчислення середнього значення функції та множення на (b - a)
    integral_mc = (b - a) * np.mean(random_y)
    return integral_mc

# Інтеграли Монте-Карло для різної кількості точок
integrals_mc = {}
for n in [100, 1000, 10000, 100000, 1000000]:
    integrals_mc[n] = monte_carlo(f, a, b, n)
    print(f"Monte Carlo інтеграл ({n} точок): {integrals_mc[n]}")

# Обчислення інтеграла 
result, error = spi.quad(f, a, b)
print("Інтеграл: ", result)

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
plt.show()
