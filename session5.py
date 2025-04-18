import numpy as np

def main():
    x_values = np.linspace(0, 2, 1000)  # 1000 values between 0 and 2
    for x in x_values:
        print(f"x: {x:.4f}, sin(x): {np.sin(x):.4f}")

main()