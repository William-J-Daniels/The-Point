import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(layout="tight")

x = np.linspace(0, 0.2, 100)
y = np.log(x)
point_x = 0.025
point_y = -1.75

ax.scatter(point_x-0.0025, point_y+0.05,
           color="red", marker="D")
ax.text(point_x, point_y, "Point",
        va="top", ha="left")

ax.plot(x, y, color="#1f77b4")
ax.annotate("", (x[-1], y[-1]), (x[-1]+np.diff(x[-2:])[0], y[-1]+np.diff(y[-2:])[0]),
            arrowprops=dict(arrowstyle="<|-, head_width=0.5", color="#1f77b4"))
ax.text(0.18, -1.85, "You")

ax.set_ylim([-4, -1])
ax.set_xticks([])
ax.set_yticks([])

fig.savefig("original.png")
plt.show()
