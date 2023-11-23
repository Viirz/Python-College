import numpy as np

def linear_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean)**2)
    a1 = numerator / denominator
    a0 = y_mean - a1 * x_mean
    
    error = 0

    for yi, xi in zip(y, x):
        error += np.square(yi - a0 - a1 * xi)

    return a1, a0, error

def main():
    n = int(input("Masukkan jumlah nilai yang akan di input (n): "))
    
    x = np.zeros(n)
    y = np.zeros(n)

    print("Masukkan nilai xi dan yi:")
    for i in range(n):
        x[i] = float(input(f"x[{i + 1}]: "))
        y[i] = float(input(f"y[{i + 1}]: "))
    
    # Hitung koefisien regresi
    a1, a0, error = linear_regression(x, y)

    # Hitung statistik
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    sum_xi_yi = np.sum(x * y)
    sum_xi_squared = np.sum(x**2)
    sum_xi = np.sum(x)
    
    # Tampilkan hasil statistik
    print(f"\nn = {n}")
    print(f"Σxiyi   = \t{sum_xi_yi}")
    print(f"Σ(xi)^2 = \t{sum_xi_squared}")
    print(f"Σxi = {sum_xi}  x̄ = {mean_x}")
    print(f"Σyi = {np.sum(y)}  ȳ = {mean_y}")
    
    # Tampilkan hasil koefisien regresi
    print(f"\na1 = {a1}")
    print(f"a0 = {a0}")
    print(f"error = {error}")

    # Tampilkan persamaan regresi
    print(f"\ny = {a0} + {a1}x + {error}")

if __name__ == "__main__":
    main()