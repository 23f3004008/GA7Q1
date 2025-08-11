# analysis.py
import matplotlib.pyplot as plt
import seaborn as sns

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
cac_values = [227.61, 228.47, 234.64, 236.61]
industry_target = 150
average_cac = sum(cac_values) / len(cac_values)

# Print the average for verification
print(f"Average CAC: {average_cac:.2f}")

# Visualization
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
bars = plt.bar(quarters, cac_values, color='skyblue', label='CAC per Quarter')
plt.axhline(industry_target, color='red', linestyle='--', label='Industry Target (150)')
plt.axhline(average_cac, color='orange', linestyle='--', label=f'Average CAC ({average_cac:.2f})')

# Add values on top of bars
for i, value in enumerate(cac_values):
    plt.text(i, value + 2, f'{value:.2f}', ha='center')

plt.title('Customer Acquisition Cost (CAC) - 2024 Quarterly Data')
plt.ylabel('CAC ($)')
plt.xlabel('Quarter')
plt.legend()
plt.tight_layout()
plt.savefig('cac_trend.png')
plt.show()
