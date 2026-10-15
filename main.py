"""
DAA Assignment: Asymptotic Notations
Run: python main.py
Requirements: matplotlib, numpy, pillow
This program animates illustrative growth rates for common complexity classes.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

n_max = 20
x = np.arange(1, n_max + 1)

fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(1, n_max)
ax.set_ylim(0, n_max**2 + 20)
ax.set_xlabel("Input size n")
ax.set_ylabel("Illustrative operation count")
ax.set_title("Comparing Asymptotic Growth Rates")
ax.grid(True, alpha=0.3)

curves = [
    ("O(1)", lambda z: np.ones_like(z, dtype=float)),
    ("O(log n)", lambda z: np.log2(z)),
    ("O(n)", lambda z: z),
    ("O(n log n)", lambda z: z * np.log2(z)),
    ("O(n²)", lambda z: z**2),
]
lines = []
for label, _ in curves:
    line, = ax.plot([], [], marker="o", markersize=3, label=label)
    lines.append(line)
ax.legend(loc="upper left")

def update(frame):
    xx = x[:frame]
    for line, (_, fn) in zip(lines, curves):
        line.set_data(xx, fn(xx))
    ax.set_title(f"Comparing Growth Rates — input size n = {frame}")
    return lines

animation = FuncAnimation(fig, update, frames=range(1, n_max + 1),
                          interval=350, blit=False, repeat=True)
animation.save("growth_rates_animation.gif", writer=PillowWriter(fps=3))
plt.show()
