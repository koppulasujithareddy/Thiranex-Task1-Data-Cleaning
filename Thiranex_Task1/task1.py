import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("titanic.csv")

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Check missing values
print(df.isnull().sum())

# Graph 1
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.show()

# Graph 2
plt.figure()
sns.countplot(x="Pclass", data=df)
plt.title("Passenger Class Distribution")
plt.show()

# Graph 3
plt.figure()
sns.countplot(x="Sex", data=df)
plt.title("Gender Distribution")
plt.show()
