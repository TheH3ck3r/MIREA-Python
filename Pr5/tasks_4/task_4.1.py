import numpy as np
import matplotlib.pyplot as plt

sprite = np.random.randint(0, 2, (5, 5))
sprite = np.maximum(sprite, sprite[:, ::-1])

plt.imshow(sprite, cmap='gray', interpolation='nearest')
plt.show()
