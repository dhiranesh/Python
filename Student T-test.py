import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as t_dist  # Using scipy only for the t-distribution curve

# Function to calculate mean
def calculate_mean(data):
    return sum(data) / len(data)

# Function to calculate variance
def calculate_variance(data, mean):
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

# Function to get critical t-value based on degrees of freedom and alpha
def get_critical_t(df, alpha=0.05):
    critical_t_values = {
        1: 12.706,
        2: 4.303,
        3: 3.182,
        4: 2.776,
        5: 2.571,
        6: 2.447,
        7: 2.365,
        8: 2.306,
        9: 2.262,
        10: 2.228,
    }
    return critical_t_values.get(df, None)

# Function to calculate t-statistic and p-value
def t_test(sample1, sample2, alpha=0.05):
    n1 = len(sample1)
    n2 = len(sample2)

    mean1 = calculate_mean(sample1)
    mean2 = calculate_mean(sample2)

    var1 = calculate_variance(sample1, mean1)
    var2 = calculate_variance(sample2, mean2)

    pooled_variance = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)
    t_statistic = (mean1 - mean2) / ((pooled_variance * (1/n1 + 1/n2)) ** 0.5)

    # Degrees of freedom
    df = n1 + n2 - 2

    # Get critical t-value for two-tailed test
    critical_t = get_critical_t(df, alpha)

    # Calculate simplified p-value
    p_value = 2 * (1 if abs(t_statistic) < critical_t else 0)

    return t_statistic, p_value, critical_t, df

# Sample data
sample1 = [23, 21, 18, 22, 25, 24]
sample2 = [23, 22, 17, 24, 26, 23]

# Calculate t-statistic and p-value
alpha = 0.05  # Change this to 0.01 for 99% confidence
t_statistic, p_value, critical_t, df = t_test(sample1, sample2, alpha)

# Display results
print(f"T-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")
print(f"Critical t-value: {critical_t:.4f}")

# Visualization of the t-distribution
x = np.linspace(-5, 5, 1000)
y = t_dist.pdf(x, df)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f't-distribution (df={df})', color='purple')

# Shade the rejection regions
plt.fill_between(x, y, where=(x <= -critical_t), color='red', alpha=0.5, label='Rejection Region')
plt.fill_between(x, y, where=(x >= critical_t), color='red', alpha=0.5)

# Mark the t-statistic
plt.axvline(t_statistic, color='blue', linestyle='dashed', linewidth=2, label='T-statistic')
plt.show()

plt.title('T-Distribution with Critical Values')
plt.xlabel('T-value')
plt.ylabel('Density')
plt.grid()