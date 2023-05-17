import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j1  # Bessel function of the first kind of order one

plt.rcParams['font.family'] = 'serif'

# Define the parameters for the airy disk
I0 = 1.0  # peak intensity
k = 3.0  # scaling factor

# Create a grid of points
x = np.linspace(-1, 1, 400)
y = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x, y)

# Calculate the radial distance from the center
r = np.sqrt(X**2 + Y**2)

# Calculate the intensity of the light at each point
I = I0 * (2 * j1(k * r) / (k * r))**2
# At r=0 this formula gives a NaN due to the 0/0 form, so we manually set the center to the peak intensity
I[np.isnan(I)] = I0

# Display the airy disk
plt.imshow(I, cmap='hot', interpolation='nearest', extent=(-1, 1, -1, 1))
plt.colorbar(label='Intensity')
plt.title('Airy Disk Pattern')


plt.savefig("airy_disk.jpg", dpi=300)