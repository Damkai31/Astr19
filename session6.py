# Cell 1: Imports
import numpy as np

# Cell 2: Define sin(x)
def sin_function(x):
    return np.sin(x)

# Cell 3: Define cos(x)
def cos_function(x):
    return np.cos(x)

# Cell 4: Tabulate and print
def main():
    x_values = np.linspace(0, 2, 1000)
    sin_values = sin_function(x_values)
    cos_values = cos_function(x_values)

    print(f"{'x':>6} {'sin(x)':>10} {'cos(x)':>10}")
    for i in range(10):
        print(f"{x_values[i]:6.4f} {sin_values[i]:10.4f} {cos_values[i]:10.4f}")

main()