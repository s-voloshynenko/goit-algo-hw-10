import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

a = 0 # Нижня межа
b = 2 # Верхня межа

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

# Графік інтегрування та випадкових точок
def draw_graph(inside_points):
    x_inside, y_inside = zip(*inside_points)
    x_outside, y_outside = zip(*[(x, y) for (x, y) in points if (x, y) not in inside_points])

    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, "r", linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))

    plt.scatter(x_inside, y_inside, color="green", s=1, label="Точки під кривою")
    plt.scatter(x_outside, y_outside, color="red", s=1, label="Точки над кривою")
    plt.legend()
    plt.grid()
    plt.show()

def is_inside(x_random, y_random):
    """Перевіряє, чи знаходиться точка Y всередині площі інтеграла."""
    return y_random < f(x_random)

# Генерація випадкових точок
points_number = 10000 # кількість точок для метода Монте-Карло
points = [(random.uniform(a, b), random.uniform(0, f(b))) for _ in range(points_number)] # x, y
inside_points = [point for point in points if is_inside(point[0], point[1])] # точки котрі потрапили всередину інтеграла

N = len(points)
M = len(inside_points)

# Теоритична площа
S, SE = spi.quad(f, a, b)
print(f"Теоритична площа інтегралу: {S} з похибкою {SE}")

# Площа за методом Монте-Карло
Sm = (M / N) * (b - a) * (f(b) - 0)
print(f"Площа інтегралу за методом Монте-Карло: {Sm}")

# Граф з точками
draw_graph(inside_points)
