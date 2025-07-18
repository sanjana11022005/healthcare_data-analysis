

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("healthcare_dataset.csv")

# Convert date columns
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])

# Add derived column
df['Length of Stay'] = (df['Discharge Date'] - df['Date of Admission']).dt.days

# Summary statistics
print(df.describe(include='all'))

# Set up visualization
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# Age distribution
plt.subplot(2, 3, 1)
sns.histplot(df['Age'], bins=30, kde=True, color='skyblue')
plt.title("Age Distribution")

# Gender distribution
plt.subplot(2, 3, 2)
sns.countplot(data=df, x='Gender', palette='pastel')
plt.title("Gender Distribution")

# Top 10 Medical Conditions
plt.subplot(2, 3, 3)
top_conditions = df['Medical Condition'].value_counts().head(10)
sns.barplot(x=top_conditions.values, y=top_conditions.index, palette='magma')
plt.title("Top 10 Medical Conditions")

# Admission Type
plt.subplot(2, 3, 4)
sns.countplot(data=df, x='Admission Type', palette='Set2')
plt.title("Admission Type")

# Avg Billing by Insurance
plt.subplot(2, 3, 5)
avg_billing = df.groupby('Insurance Provider')['Billing Amount'].mean().sort_values(ascending=False).head(5)
sns.barplot(x=avg_billing.values, y=avg_billing.index, palette='coolwarm')
plt.title("Avg Billing by Insurance Provider")

# Monthly Admission Trends
plt.subplot(2, 3, 6)
monthly_trend = df['Date of Admission'].dt.to_period('M').value_counts().sort_index()
monthly_trend.plot(kind='line', marker='o', color='teal')
plt.title("Monthly Admission Trend")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
