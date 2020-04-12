import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split


class Student:
    # Constructor
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    # Function to create and append new student
    def accept(self, Name, Rollno, marks1, marks2):
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)

    # Function to display student details
    def display(self, ob):
        print("Name : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n")

    # Create a list to add Students


ls = []
# an object of Student class
obj = Student('', 0, 0, 0)

obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)

print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])

print("Thank You !")

df = pd.read_csv(‘student-mat.csv’)
df.head()

# Histogram of grades
plt.hist(df['Grade'], bins = 14)
plt.xlabel('Grade')
plt.ylabel('Count')
plt.title('Distribution of Final Grades')

# Make one plot for each different location
sns.kdeplot(df.ix[df['address'] == 'U', 'Grade'],
            label = 'Urban', shade = True)
sns.kdeplot(df.ix[df['address'] == 'R', 'Grade'],
            label = 'Rural', shade = True)
# Add labeling
plt.xlabel('Grade')
plt.ylabel('Density')
plt.title('Density Plot of Final Grades by Location')
# Find correlations and sort
df.corr()['Grade'].sort_values()
# Select only categorical variables
category_df = df.select_dtypes('object')
# One hot encode the variables
dummy_df = pd.get_dummies(category_df)
# Put the grade back in the dataframe
dummy_df['Grade'] = df['Grade']
# Find correlations with grade
dummy_df.corr()['Grade'].sort_values()
# df is features and labels are the targets
# Split by putting 25% in the testing set
X_train, X_test, y_train, y_test = train_test_split(df, labels, test_size = 0.25, random_state=42)
# X_train is our training data, we will make a copy for plotting
X_plot = X_train.copy()
# Compare grades to the median
X_plot['relation_median'] = (X_plot['Grade'] >= 12)
X_plot['Grade'] = X_plot['Grade'].replace({True: 'above',
                                           False: 'below'})
# Plot all variables in a loop
plt.figure(figsize=(12, 12))
for i, col in enumerate(X_plot.columns[:-1]):
    plt.subplot(3, 2, i + 1)
    subset_above = X_plot[X_plot['relation_median'] == 'above']
    subset_below = X_plot[X_plot['relation_median'] == 'below']
    sns.kdeplot(subset_above[col], label='Above Median')
    sns.kdeplot(subset_below[col], label='Below Median')
    plt.legend()
    plt.title('Distribution of %s' % col)

plt.tight_layout()