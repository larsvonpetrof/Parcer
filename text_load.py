# Loading text via numpy

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("https://video.ittensive.com/python-advanced/01.mnist.8.txt", \
                  delimiter=",")
data = np.reshape(data[1], (28,28))
plt.imshow(data, cmap="Greys")
plt.show()

