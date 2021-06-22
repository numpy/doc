# From Dalgaard page 83 [R755c9bae090e-1]_, suppose the daily energy intake for 11
# women in kilojoules (kJ) is:

intake = np.array([5260., 5470, 5640, 6180, 6390, 6515, 6805, 7515, \
                   7515, 8230, 8770])

# Does their energy intake deviate systematically from the recommended
# value of 7725 kJ? Our null hypothesis will be the absence of deviation,
# and the alternate hypothesis will be the presence of an effect that could be
# either positive or negative, hence making our test 2-tailed.

# Because we are estimating the mean and we have N=11 values in our sample,
# we have N-1=10 degrees of freedom. We set our significance level to 95% and
# compute the t statistic using the empirical mean and empirical standard
# deviation of our intake. We use a ddof of 1 to base the computation of our
# empirical standard deviation on an unbiased estimate of the variance (note:
# the final estimate is not unbiased due to the concave nature of the square
# root).

np.mean(intake)
# 6753.636363636364
intake.std(ddof=1)
# 1142.1232221373727
t = (np.mean(intake)-7725)/(intake.std(ddof=1)/np.sqrt(len(intake)))
t
# -2.8207540608310198

# We draw 1000000 samples from Student's t distribution with the adequate
# degrees of freedom.

import matplotlib.pyplot as plt
s = np.random.standard_t(10, size=1000000)
h = plt.hist(s, bins=100, density=True)

# Does our t statistic land in one of the two critical regions found at
# both tails of the distribution?

np.sum(np.abs(t) < np.abs(s)) / float(len(s))
# 0.018318  #random < 0.05, statistic is in critical region

# The probability value for this 2-tailed test is about 1.83%, which is
# lower than the 5% pre-determined significance threshold.

# Therefore, the probability of observing values as extreme as our intake
# conditionally on the null hypothesis being true is too low, and we reject
# the null hypothesis of no deviation.
