import numpy as np
####
# Example data
m2 = np.random.normal(10, 2, 1000)  # Simulated m2 values
mk2 = m2 * 0.8 + np.random.normal(0, 1, 1000)  # Simulated dependent mk2 values

# Covariance and Pearson correlation
covariance = np.cov(m2, mk2)[0, 1]
pearson_corr = np.corrcoef(m2, mk2)[0, 1]

print(f"Covariance: {covariance}")
print(f"Pearson Correlation: {pearson_corr}")

# Scatter plot for visual inspection
import matplotlib.pyplot as plt

plt.scatter(m2, mk2, alpha=0.5)
plt.xlabel('m2')
plt.ylabel('mk2')
plt.title('Scatter plot of m2 vs mk2')
plt.show()
