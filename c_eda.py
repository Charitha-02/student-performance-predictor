import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("d_data/StudentsPerformance.csv")

# Show basic info
print("Dataset Info:")
print(data.info())

# Describe the data
print("\nStatistical Summary:")
print(data.describe())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Plot distribution of scores
plt.figure(figsize=(10, 6))
sns.histplot(data["math score"], kde=True, color="skyblue", label="Math Score")
sns.histplot(data["reading score"], kde=True, color="lightgreen", label="Reading Score")
sns.histplot(data["writing score"], kde=True, color="salmon", label="Writing Score")
plt.title("Distribution of Scores")
plt.legend()
plt.tight_layout()
plt.show()

# Box plots for gender vs scores
plt.figure(figsize=(12, 4))
for idx, subject in enumerate(["math score", "reading score", "writing score"]):
    plt.subplot(1, 3, idx + 1)
    sns.boxplot(data=data, x="gender", y=subject)
    plt.title(f"{subject} by Gender")
plt.tight_layout()
plt.show()
