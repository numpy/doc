import matplotlib.pyplot as plt
np.kaiser(12, 14)
# array([  7.72686684e-06,   3.46009194e-03,   4.65200189e-02,
# 2.29737120e-01,   5.99885316e-01,   9.45674898e-01,
# 9.45674898e-01,   5.99885316e-01,   2.29737120e-01,
# 4.65200189e-02,   3.46009194e-03,   7.72686684e-06])

# Plot the window and the frequency response:

from numpy.fft import fft, fftshift
window = np.kaiser(51, 14)
plt.plot(window)
# [<matplotlib.lines.Line2D object at 0x...>]
plt.title("Kaiser window")
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
plt.title("Frequency response of Kaiser window")
# <matplotlib.text.Text object at 0x...>
plt.ylabel("Magnitude [dB]")
# <matplotlib.text.Text object at 0x...>
plt.xlabel("Normalized frequency [cycles per sample]")
# <matplotlib.text.Text object at 0x...>
plt.axis('tight')
# (-0.5, 0.5, -100.0, ...)
plt.show()
