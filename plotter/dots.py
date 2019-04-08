import matplotlib

matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]

import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
import numpy as np

fig = plt.figure(1, figsize=(5.5, 5.5))

ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>", size=2)
    ax.axis[direction].line.set_facecolor("black")
    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)
    
    ax.set_xticks([])
    ax.set_yticks([])

ax.set_ylim(-1.1, 1.3)
ax.set_xlim(-1.3, 1.3)

ax.axis['yzero'].major_ticklabels.set_axis_direction('right')

centreCircle = plt.Circle((0, 0), 1, color="black", fill=False, lw=2, alpha=.9)

# Draw the circles to our plot
ax.add_patch(centreCircle)
ax.set_aspect("equal", adjustable="box")

for direction in ["left", "right", "bottom", "top"]:
    # hides borders
    ax.axis[direction].set_visible(False)

plt.text(1.25, 0.05, r'$ \boldsymbol{X}$', fontsize=16, fontweight='bold')
plt.text(0.05, 1.25, r'$ \boldsymbol{Y}$', fontsize=16, fontweight='bold')

plt.text(-0.1, 0.05, r'$ \boldsymbol{0}$', fontsize=16, fontweight='heavy')
plt.text(1.05, 0.05, r'$ \boldsymbol{1}$', fontsize=16, fontweight='bold')
plt.text(0.05, 1.05, r'$ \boldsymbol{1}$', fontsize=16, fontweight='bold')
plt.text(-0.95, 0.05, r'$ \boldsymbol{-1}$', fontsize=16, fontweight='bold')
plt.text(0.05, -0.95, r'$ \boldsymbol{-1}$', fontsize=16, fontweight='bold')

x, y = 0, 1

ax.hlines(y=y, xmin=0, xmax=x, linewidth=1.5, color='r', linestyles='dashed')
ax.vlines(x=x, ymin=0, ymax=y, linewidth=1.5, color='b', linestyles='dashed')

plt.plot(x, 0, 'bo')
# plt.text(x, 0, r'$ \boldsymbol{\frac{1}{2}} $', position=(x, -0.24), fontsize=20, fontweight='bold')
plt.plot(0, y, 'ro')
# plt.text(0, y, r'$ \boldsymbol{\frac{\sqrt{3}}{2}} $', position=(-0.23, y-0.13), fontsize=20, fontweight='bold')

plt.plot(x, y, 'ko', markersize=4)
# plt.text(0, y, r'$ \boldsymbol{(0, 1)} $', position=(x+0.1, y-0.05), fontsize=20, fontweight='bold')

x1 = np.random.uniform(low=-1, high=1.0, size=30)
y1 = np.sqrt(1 - x1 ** 2)

x2 = np.random.uniform(low=-1, high=1.0, size=30)
y2 = -np.sqrt(1 - x2 ** 2)

plt.scatter(x1, y1, s=50, c=x1+y1, cmap=plt.get_cmap("seismic"))
plt.scatter(x2, y2, s=50, c=x2+y2, cmap=plt.get_cmap("seismic"))

plt.show()
