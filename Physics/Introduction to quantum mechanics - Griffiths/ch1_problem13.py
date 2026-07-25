import numpy as np
import matplotlib.pyplot as plt

def pos(t, A, omega):
    omega = 2 * np.pi * omega
    return A * np.cos(omega *t)

def rho(x, A):
    return 1 / (np.pi * np.sqrt(A**2 - x**2))

A = 1
omega = 1

t = np.random.random(10_000)

x = pos(t, A, omega)

position = np.linspace(-0.999, 0.999, 10_000)

plt.figure(figsize=(7, 4.5))
plt.hist(x, bins=100, density=True, color="lightsteelblue", edgecolor="white", 
         linewidth=0.5, alpha=0.8, label="numerical")

plt.plot(position, rho(position, A), color="black", linewidth=2.5, label="Theory")

plt.xlim(-1, 1)
plt.ylim(0, 2)

plt.xlabel("Position $x$", fontsize=12)
plt.ylabel("Probability density", fontsize=12)

plt.legend(frameon=False)
plt.grid(alpha=0.25)

plt.tight_layout()
plt.show()

