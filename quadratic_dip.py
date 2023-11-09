import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(layout="tight")

you_dip = -0.1
x = np.linspace(-1, 0.9, 100)
y = -x**2 + you_dip*np.exp(-x**2/(2*0.05**2))
point_x = 0
point_y = 0

ax.scatter(point_x, point_y,
           color="red", marker="D")
ax.text(point_x, point_y+0.05, "Point",
        va="bottom", ha="center")

ax.plot(x, y, color="#1f77b4")
ax.annotate("", (x[-2], y[-2]), (x[-1]+np.diff(x[-2:])[0], y[-1]+np.diff(y[-2:])[0]),
            arrowprops=dict(arrowstyle="<|-, head_width=0.5", color="#1f77b4"))
ax.text(0, you_dip-0.05, "You",
        va="top", ha="center")

ax.set_ylim([-1.0, 0.1])
ax.set_xlim([-1.1, 1.1])
ax.set_xticks([])
ax.set_yticks([])

fig.savefig("quadratic_dip.png")
plt.show()
