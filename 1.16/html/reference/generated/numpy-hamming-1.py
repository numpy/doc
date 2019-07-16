np.hamming(12)
# array([ 0.08      ,  0.15302337,  0.34890909,  0.60546483,  0.84123594,
# 0.98136677,  0.98136677,  0.84123594,  0.60546483,  0.34890909,
# 0.15302337,  0.08      ])

# Plot the window and the frequency response:

import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
window = np.hamming(51)
plt.plot(window)
# [<matplotlib.lines.Line2D object at 0x...>]
plt.title("Hamming window")
# <matplotlib.text.Text object at 0x...>
plt.ylabel("Amplitude")
# <matplotlib.text.Text object at 0x...>
plt.xlabel("Sample")
# <matplotlib.text.Text object at 0x...>
plt.show()

plt.figure()
# <matplotlib.figure.Figure object at 0x...>
A = fft(window, 2048) / 25.5
mag = np.abs(fftshift(A))
freq = np.linspace(-0.5, 0.5, len(A))
response = 20 * np.log10(mag)
response = np.clip(response, -100, 100)
plt.plot(freq, response)
# [<matplotlib.lines.Line2D object at 0x...>]
plt.title("Frequency response of Hamming window")
# <matplotlib.text.Text object at 0x...>
plt.ylabel("Magnitude [dB]")
# <matplotlib.text.Text object at 0x...>
plt.xlabel("Normalized frequency [cycles per sample]")
# <matplotlib.text.Text object at 0x...>
plt.axis('tight')
# (-0.5, 0.5, -100.0, ...)
plt.show()
