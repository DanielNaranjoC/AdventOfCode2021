import matplotlib.pyplot as plt
from main import lines
for i, j in lines:
    plt.plot(i, j, 'k', linewidth=0.2)
plt.axis('off')
plt.show()
