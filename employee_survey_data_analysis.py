# -*- coding: utf-8 -*-
"""Employee_Survey_Data_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MZrB6QL8rwp_n-lQdOwaPYis9ThozGJq
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/employee_survey.csv')

# Basic Statistical Summary
print("Basic Statistical Summary:\n", df.describe())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Distribution of numeric features
numeric_columns = ['Age', 'Experience', 'WLB', 'WorkEnv', 'PhysicalActivityHours', 'Workload', 'Stress', 'SleepHours', 'CommuteDistance', 'TrainingHoursPerYear', 'JobSatisfaction']

# Plot distribution of numeric columns
df[numeric_columns].hist(figsize=(15, 10), bins=20, edgecolor='black')
plt.suptitle("Distribution of Numeric Features")
plt.show()

# Analyzing average JobSatisfaction by Department
dept_satisfaction = df.groupby('Dept')['JobSatisfaction'].mean().sort_values()

# Plot average JobSatisfaction by Department
plt.figure(figsize=(10, 6))
dept_satisfaction.plot(kind='bar', color='skyblue')
plt.title('Average Job Satisfaction by Department')
plt.ylabel('Job Satisfaction')
plt.xlabel('Department')
plt.show()

# Analyzing the impact of Work-Life Balance on Job Satisfaction
plt.figure(figsize=(8, 6))
df.boxplot(column='JobSatisfaction', by='WLB')
plt.title('Job Satisfaction by Work-Life Balance')
plt.suptitle('')  # Suppress the default title
plt.show()

# Average JobSatisfaction by Gender
gender_satisfaction = df.groupby('Gender')['JobSatisfaction'].mean()

# Plot average JobSatisfaction by Gender
plt.figure(figsize=(8, 6))
gender_satisfaction.plot(kind='bar', color='lightgreen')
plt.title('Average Job Satisfaction by Gender')
plt.ylabel('Job Satisfaction')
plt.xlabel('Gender')
plt.show()