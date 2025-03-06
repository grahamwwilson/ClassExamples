# MyKSTest.py
from scipy.stats import kstest

# Desired CDF F(x) = (3/2)(x - x^3 / 3)
def desired_cdf(x):
    return (3/2) * (x - x**3 / 3)
    
# Kolmogorov-Smirnov test function
def ks_test(samples):
    
    # Perform the KS test (comparing the empirical CDF with theoretical CDF)
    ks_statistic, p_value = kstest(samples, desired_cdf, method='exact')
    
    return ks_statistic, p_value
    
def runKSTest(samples):

    print(' ')
    print('Now run KS test on the sampled x values')
    print(' ')

# Run KS test on the sampled x values to check if consistent with desired distirbution
    ks_statistic, p_value = ks_test(samples)

# Print the result
    print(f"KS Statistic: {ks_statistic}")
    print(f"P-value: {p_value}")

# Interpretation of the result
    if p_value > 0.05:
        print("Fail to reject the null hypothesis at 5% significance level => samples are consistent with the desired distribution.")
    else:
        print("The null hypothesis is rejected at the 5% significance level => samples are not consistent with the desired distribution.")

