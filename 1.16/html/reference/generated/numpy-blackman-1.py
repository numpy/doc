import matplotlib.pyplot as plt
np.blackman(12)
# array([ -1.38777878e-17,   3.26064346e-02,   1.59903635e-01,
# 4.14397981e-01,   7.36045180e-01,   9.67046769e-01,
# 9.67046769e-01,   7.36045180e-01,   4.14397981e-01,
# 1.59903635e-01,   3.26064346e-02,  -1.38777878e-17])

# Plot the window and the frequency response:

from numpy.fft import fft, fftshift
window = np.blackman(51)
plt.plot(window)
# [<matplotlib.lines.Line2D object at 0x...>]
plt.title("Blackman window")
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
plt.title("Frequency response of Blackman window")
# <matplotlib.text.Text object at 0x...>
plt.ylabel("Magnitude [dB]")
# <matplotlib.text.Text object at 0x...>
plt.xlabel("Normalized frequency [cycles per sample]")
# <matplotlib.text.Text object at 0x...>
plt.axis('tight')
# (-0.5, 0.5, -100.0, ...)
plt.show()
