# titanic_visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
df = pd.read_csv("titanic.csv")

# Show basic info
print("Dataset Shape:", df.shape)
print("First 5 rows:\n", df.head())

# Visualization 1: Survival Count
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Survived', palette='Set2')
plt.title("Survival Count (0 = Died, 1 = Survived)")
plt.xlabel("Survived")
plt.ylabel("Passenger Count")
plt.show()

# Visualization 2: Survival by Sex
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Sex', hue='Survived', palette='Set1')
plt.title("Survival by Gender")
plt.ylabel("Count")
plt.show()

# Visualization 3: Age Distribution
plt.figure(figsize=(8,4))
sns.histplot(df['Age'].dropna(), kde=True, bins=30, color='teal')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Visualization 4: Class vs Survival
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Pclass', hue='Survived', palette='Pastel1')
plt.title("Passenger Class vs Survival")
plt.show()
