import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Sample Machine Data (replace with your actual data)
data = {'MachineID': ['M1', 'M2', 'M3'],
        'Age (months)': [12, 24, 6],
        'Usage (hours)': [1000, 2000, 500],
        'LastMaintenance': [datetime(2023, 1, 1), datetime(2022, 12, 15), datetime(2023, 2, 1)],
        'MaintenanceCost': [500, 750, 300],
        'DowntimeCostPerHour': [1000, 1200, 800]}
df = pd.DataFrame(data)

# 2. Simplified Rule-Based Scheduling (example)
def schedule_maintenance(row):
    if row['Age (months)'] > 18 or row['Usage (hours)'] > 1500:
        return row['LastMaintenance'] + timedelta(days=90)  # Schedule maintenance in 3 months
    else:
        return row['LastMaintenance'] + timedelta(days=180) # Schedule maintenance in 6 months

df['NextMaintenance'] = df.apply(schedule_maintenance, axis=1)

print(df)


# 3. Cost-Based Optimization (highly simplified example - needs more data and a proper optimization algorithm)
# In a real-world scenario, you would need historical breakdown data to estimate probabilities.
# You would then use an optimization algorithm to minimize the expected cost.

# Example: calculate expected cost for M1 (highly simplified)
# Assume probability of breakdown in next 3 months is 0.1 (this would come from a predictive model)
probability_breakdown = 0.1
expected_cost_m1 = (df['MaintenanceCost'][0] * (1 - probability_breakdown)) + (df['DowntimeCostPerHour'][0] * 24 * 7 * probability_breakdown) # Simplified cost calculation (7 days of downtime if breakdown occurs)

print(f"\nExpected Cost for M1 (Simplified): {expected_cost_m1}")
