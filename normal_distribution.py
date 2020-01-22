import numpy as np
import matplotlib.pyplot as plt

mu, sigma, n = 0, 0.1, 1000  # Define the mean, variance and size of the distribution

s = np.random.normal(mu, sigma, n)  # Creates a random distribution with these parameters

# We check mu and sigma are ok:
print(abs(mu - np.mean(s)))
print(abs(sigma - np.std(s,ddof=1))) # ddof=1 uses an unbaiased estimator

# First we create a histogram (s is in general an array)
count, bins, ignored = plt.hist(s, 30, density='True') # bins = number of intervals

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi))*np.exp( - (bins - mu)**2 / (2 * sigma**2)),
         linewidth = 2, color = 'r')  # We are using bins as our variable x so it's not as smooth
plt.show()
