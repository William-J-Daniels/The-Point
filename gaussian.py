import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(layout="tight")

point_x = 0.7
point_y = 0.0
x = np.linspace(0, 1, 100)
y = 0.3*np.exp(-(x-point_x)**2 / (2*0.1**2))

ax.scatter(point_x, point_y,
           color="red", marker="D")
ax.text(point_x, point_y-0.025, "Point",
        va="top", ha="center")

ax.plot(x, y, color="#1f77b4")
ax.annotate("", (x[-1], y[-1]), (x[-1]+np.diff(x[-2:])[0], y[-1]+np.diff(y[-2:])[0]),
            arrowprops=dict(arrowstyle="<|-, head_width=0.5", color="#1f77b4"))
ax.text(0.9, 0.04, "You")

ax.set_ylim([-0.1, 1.1])
ax.set_xticks([])
ax.set_yticks([])

fig.savefig("gaussian.png")
plt.show()
