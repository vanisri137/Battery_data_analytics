import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import os

os.makedirs('outputs', exist_ok=True)
df = pd.read_csv('data/cleaned/cleaned_battery_data.csv')

sns.set_theme(style='whitegrid')

# Plot 1 — Retention Rate vs Cycle Number
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='cycle_number', y='retention_rate',
                hue='test_type', alpha=0.6, palette='tab10')
plt.title('Battery Retention Rate vs Cycle Number', fontsize=14, fontweight='bold')
plt.xlabel('Cycle Number')
plt.ylabel('Retention Rate (%)')
plt.tight_layout()
plt.savefig('outputs/retention_trend.png', dpi=150)
plt.close()
print("Saved retention_trend.png")

# Plot 2 — Peak Testing Hours
hourly = df.groupby('hour').size().reset_index(name='count')
plt.figure(figsize=(10, 5))
sns.barplot(data=hourly, x='hour', y='count', palette='Blues_d')
plt.title('Test Activity by Hour of Day', fontsize=14, fontweight='bold')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Tests')
plt.tight_layout()
plt.savefig('outputs/peak_usage_chart.png', dpi=150)
plt.close()
print("Saved peak_usage_chart.png")

# Plot 3 — Capacity Distribution by Status
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='status', y='capacity', palette='Set2')
plt.title('Capacity Distribution by Test Status', fontsize=14, fontweight='bold')
plt.xlabel('Status')
plt.ylabel('Capacity (mAh)')
plt.tight_layout()
plt.savefig('outputs/performance_summary.png', dpi=150)
plt.close()
print("Saved performance_summary.png")
