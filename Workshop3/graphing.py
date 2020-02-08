import numpy as np
import matplotlib.pyplot as plt

# Our data...
x = np.linspace(0, 10, 100)
y1, y2, y3 = np.cos(x), np.cos(x + 1), np.cos(x + 2)
names = ['Signal 1', 'Signal 2', 'Signal 3']

fig, (ax1, ax2, ax3) = plt.subplots(3)

ax1.title.set_text(names[0])
ax2.title.set_text(names[1])
ax3.title.set_text(names[2])

ax1.plot(x, y1)
ax2.plot(x, y2)
ax3.plot(x, y3)

for i in [ax1, ax2, ax3]:
  i.set_xticks([])
  i.set_yticks([])
  i.set_xlim(left=0, right=10)
  i.set_ylim(bottom=-1, top=1)

plt.tight_layout()