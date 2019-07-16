# Draw samples from the distribution:

loc, scale = 10, 1
s = np.random.logistic(loc, scale, 10000)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, bins=50)

# #   plot against distribution

def logist(x, loc, scale):
    return exp((loc-x)/scale)/(scale*(1+exp((loc-x)/scale))**2)
plt.plot(bins, logist(bins, loc, scale)*count.max()/\
logist(bins, loc, scale).max())
plt.show()
