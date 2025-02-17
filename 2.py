import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    """
    Функція, яку потрібно інтегрувати.
    
    Параметри:
    x (float або np.array): Вхідне значення або масив значень.

    Повертає:
    float або np.array: Значення функції f(x) = x^2.
    """
    return x ** 2

# Межі інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

def monte_carlo_integral(f, a, b, N=100000):
    """
    Обчислює визначений інтеграл функції методом Монте-Карло.

    Параметри:
    f (function): Функція, яку потрібно інтегрувати.
    a (float): Нижня межа інтегрування.
    b (float): Верхня межа інтегрування.
    N (int, optional): Кількість випадкових точок (за замовчуванням 100000).

    Повертає:
    float: Приблизне значення інтегралу.
    """
    x_random = np.random.uniform(a, b, N)
    y_random = np.random.uniform(0, f(b), N)
    points_under_curve = np.sum(y_random < f(x_random))
    area = (b - a) * f(b) * (points_under_curve / N)
    return area

# Обчислення інтегралу методом Монте-Карло
monte_carlo_result = monte_carlo_integral(f, a, b)

# Аналітичне обчислення інтегралу
def analytical_integral(f, a, b):
    """
    Обчислює визначений інтеграл функції аналітично за допомогою SciPy.

    Параметри:
    f (function): Функція, яку потрібно інтегрувати.
    a (float): Нижня межа інтегрування.
    b (float): Верхня межа інтегрування.

    Повертає:
    tuple: (значення інтегралу, оцінка абсолютної похибки).
    """
    result, error = spi.quad(f, a, b)
    return result, error

result_quad, error_quad = analytical_integral(f, a, b)

def plot_integration(f, a, b, x_random, y_random):
    """
    Побудова графіка функції з областю під інтегралом та точками Монте-Карло.

    Параметри:
    f (function): Функція, яку потрібно інтегрувати.
    a (float): Нижня межа інтегрування.
    b (float): Верхня межа інтегрування.
    x_random (np.array): Масив випадкових x-координат для методу Монте-Карло.
    y_random (np.array): Масив випадкових y-координат для методу Монте-Карло.
    """
    x_values = np.linspace(a - 0.5, b + 0.5, 400)
    y_values = f(x_values)

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, 'r', linewidth=2, label="f(x) = x^2")

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Точки методу Монте-Карло
    ax.scatter(x_random[:1000], y_random[:1000], s=1, color="blue", alpha=0.3, label="Точки Монте-Карло")

    # Межі інтегрування
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')

    # Налаштування графіка
    ax.set_xlim([x_values[0], x_values[-1]])
    ax.set_ylim([0, max(y_values) + 0.5])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Метод Монте-Карло для обчислення інтегралу')
    ax.legend()
    plt.grid()
    plt.show()

# Виведення результатів
print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Аналітичний метод (quad): {result_quad}, Похибка: {error_quad}")

# Візуалізація результатів
plot_integration(f, a, b, np.random.uniform(a, b, 1000), np.random.uniform(0, f(b), 1000))


