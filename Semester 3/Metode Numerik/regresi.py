import numpy as np

def linear_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean)**2)
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    return slope, intercept

def main():
    n = int(input("Masukkan jumlah pasangan nilai (n): "))
    
    x = np.zeros(n)
    y = np.zeros(n)

    print("Masukkan nilai xi dan yi:")
    for i in range(n):
        x[i] = float(input(f"x[{i + 1}]: "))
        y[i] = float(input(f"y[{i + 1}]: "))
    
    # Hitung koefisien regresi
    slope, intercept = linear_regression(x, y)

    # Hitung statistik
    x_bar = np.mean(x)
    y_bar = np.mean(y)
    sum_xi_yi = np.sum(x * y)
    sum_xi_squared = np.sum(x**2)
    sum_xi = np.sum(x)
    
    # Tampilkan hasil statistik
    print(f"\nn = {n}")
    print(f"Σxiyi   = \t{sum_xi_yi}")
    print(f"Σ(xi)^2 = \t{sum_xi_squared}")
    print(f"Σxi = {sum_xi}  x̄ = {x_bar}")
    print(f"Σyi = {np.sum(y)}  ȳ = {y_bar}")
    
    # Tampilkan hasil koefisien regresi
    print(f"\na1 = {slope}")
    print(f"a0 = {intercept}")

    # Tampilkan persamaan regresi
    print(f"\ny = {intercept} + {slope}x")

if __name__ == "__main__":
    main()