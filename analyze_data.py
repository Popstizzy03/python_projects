import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
csv_file = 'large_data.csv'
df = pd.read_csv(csv_file)

# Display basic information about the dataset
print("Dataset Overview:")
print(df.info())
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())

# Analysis: Average salary by department
avg_salary_by_dept = df.groupby('department')['salary'].mean()
print("\nAverage Salary by Department:")
print(avg_salary_by_dept)

# Visualization: Bar chart of average salary by department
plt.figure(figsize=(10, 6))
avg_salary_by_dept.plot(kind='bar', color='skyblue')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Analysis: Age distribution
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Analysis: Top 10 highest salaries
top_salaries = df.nlargest(10, 'salary')[['name', 'salary', 'department']]
print("\nTop 10 Highest Salaries:")
print(top_salaries)

# Visualization: Pie chart of department distribution
dept_distribution = df['department'].value_counts()
plt.figure(figsize=(8, 8))
dept_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Department Distribution')
plt.ylabel('')
plt.show()