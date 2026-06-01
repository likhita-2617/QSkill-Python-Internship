import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD THE CSV FILE
# This reads your file and turns it into a structured table called a DataFrame
df = pd.read_csv('student_data.csv')
print("--- Dataset Loaded Successfully ---")
print(df)
print("\n")

# 2. PERFORM BASIC DATA ANALYSIS
# We will calculate the average (mean) of the 'Score' column
average_score = df['Score'].mean()
average_hours = df['Hours_Studied'].mean()

print(f"Average Exam Score: {average_score:.2f}%")
print(f"Average Hours Studied: {average_hours:.2f} hours")
print("\n")

# 3. CREATE VISUALIZATIONS

# Chart A: Bar Chart (Student vs Exam Score)
plt.figure(figsize=(6, 4))
plt.bar(df['Student'], df['Score'], color='skyblue')
plt.title('Exam Scores by Student')
plt.xlabel('Student Name')
plt.ylabel('Exam Score (%)')
plt.savefig('bar_chart.png') # Saves the chart as an image
plt.close()

# Chart B: Scatter Plot (Hours Studied vs Exam Score)
plt.figure(figsize=(6, 4))
plt.scatter(df['Hours_Studied'], df['Score'], color='purple', s=100)
plt.title('Hours Studied vs. Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score (%)')
plt.grid(True)
plt.savefig('scatter_plot.png')
plt.close()

# Chart C: Heatmap (Correlation between numerical columns)
plt.figure(figsize=(6, 4))
# We select only columns with numbers for a heatmap
numeric_df = df[['Hours_Studied', 'Score', 'Attendance_Pct']]
# .corr() calculates how closely related the numbers are
correlation_matrix = numeric_df.corr() 

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')
plt.close()

print("Charts generated and saved as images successfully!")