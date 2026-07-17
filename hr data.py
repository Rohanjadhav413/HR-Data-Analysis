import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib .pyplot as plt


df = pd.read_excel("C:\\Users\\rj973\\Downloads\\HR Data.xlsx")
#first 5 rows
print(df.head())
#last 5 rows
print(df.tail())



# Dataset information
print(df.info())


#shape
print(df.shape)

#column
print(df.columns)

#missing values
print(df.isnull().sum())

#duplicate values
print(df.duplicated().sum())

#statstical summary
print(df.describe())

#check missing values
print(df.isnull().sum())

#fill missing values
df = df.fillna(df.mean(numeric_only=True))
print(df.isnull().sum())


#remove duplicate
df = df.drop_duplicates()
print(df.duplicated().sum())

# KPI Summary
print("Total Employees :", len(df))
print("Average Age :", round(df["Age"].mean(),2))
print("Average Monthly Income :", round(df["Monthly Income"].mean(),2))
print("Attrition Rate :", round((df["Attrition"]=="Yes").mean()*100,2), "%")

# Top 5 Highest Salary Employees
print(df.nlargest(5, "Monthly Income")[["Employee Number", "Job Role", "Monthly Income"]])

# Top 5 Lowest Salary Employees
print(df.nsmallest(5, "Monthly Income")[["Employee Number", "Job Role", "Monthly Income"]])

# Department-wise Attrition
print(pd.crosstab(df["Department"], df["Attrition"]))

# Department-wise Attrition Graph
sns.countplot(
    x="Department",
    hue="Attrition",
    data=df
)

plt.title("Department-wise Attrition")
plt.xticks(rotation=30)
plt.show()





# ==========================
# Overtime Percentage
# ==========================

print(df["Over Time"].value_counts(normalize=True)*100)
sns.countplot(
    x="Over Time",
    data=df
)

plt.title("Over Time Employees")
plt.show()

#check data type
print(df.dtypes)

#unique values
print(df["Department"].unique())

#count unique values
print(df["Department"].value_counts())

print(df.columns.tolist())

#numpy
print(np.mean(df["Monthly Income"]))
print(np.median(df["Monthly Income"]))
print(np.max(df["Monthly Income"]))
print(np.min(df["Monthly Income"]))
print(np.std(df["Monthly Income"]))




#Gender Distribution
#pie chart
gender = df["Gender"].value_counts()

plt.pie(
    gender,
    labels=gender.index,
    colors=["skyblue", "pink"],
    explode=[0.0, 0.1],
    autopct="%1.2f%%",
    shadow=True,
    startangle=90,
    radius=1,
    labeldistance=1.2,
    rotatelabels=True,
    textprops={"fontsize":10, "color":"black"},
    wedgeprops={"lw":2, "edgecolor":"white"},
    counterclock=False
)

plt.title("Gender Distribution")
plt.legend()
plt.show()

# Attrition Percentage
attr = df["Attrition"].value_counts()

plt.pie(
    attr,
    labels=attr.index,
    autopct="%1.1f%%",
    colors=["lightgreen","tomato"]
)

plt.title("Attrition Percentage")
plt.show()
#Department vs Average Monthly Income:
#line chart
dept = df.groupby("Department")["Monthly Income"].mean()

plt.plot(
    dept.index,
    dept.values,
    color="red",
    linestyle="dotted",
    marker="*",
    mfc="green",
    mec="black",
    ms=15,
    alpha=1,
    label="Average Monthly Income"
)

plt.xlabel("Department", color="red", fontsize=15)
plt.ylabel("Average Income", color="blue", fontsize=15)
plt.title("Department Wise Average Monthly Income")
plt.legend()
plt.grid()
plt.show()

#grouped bar chart
#Department-wise Male vs Female Employees:
dept = df["Department"].unique()

male = df[df["Gender"] == "Male"].groupby("Department").size()
female = df[df["Gender"] == "Female"].groupby("Department").size()

width = 0.35
a = np.arange(len(dept))
x = a + width

plt.bar(a, male.reindex(dept, fill_value=0), width=width, color="blue", label="Male")
plt.bar(x, female.reindex(dept, fill_value=0), width=width, color="pink", label="Female")

plt.xticks(a + width/2, dept)
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.title("Department-wise Male vs Female Employees")
plt.legend()
plt.show()

#count plot
#attrition analysis
print(df["Attrition"].value_counts())
sns.countplot(x="Attrition", data=df)
plt.title("Employee Attrition")
plt.show()

#histogram
#age distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Age"], bins=15)
plt.title("Age Distribution")
plt.show()
# ==========================
# Job Role Wise Average Salary
# ==========================

print(df.groupby("Job Role")["Monthly Income"].mean().sort_values(ascending=False))


# ==========================
# Age Group Analysis
# ==========================

bins=[18,25,35,45,60]
labels=["18-25","26-35","36-45","46-60"]

df["Age Group"]=pd.cut(df["Age"],bins=bins,labels=labels)

print(df["Age Group"].value_counts())

sns.countplot(
    x="Age Group",
    data=df
)

plt.title("Employee Age Groups")
plt.show()


#histogram
#monthly income distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Monthly Income"], bins=20)
plt.title("Monthly Income Distribution")
plt.show()




#
#department wise average monthly income
#histogram
print(df.groupby("Department")["Monthly Income"].mean())

sns.barplot(
    x="Department",
    y="Monthly Income",
    data=df,
    estimator="mean"
)
plt.title("Average Monthly Income by Department")
plt.show()

# ==========================
# Gender-wise Average Salary
# ==========================

print(df.groupby("Gender")["Monthly Income"].mean())
sns.boxplot(
    x="Gender",
    y="Monthly Income",
    data=df
)

plt.title("Monthly Income by Gender")
plt.show()

#job role analysis
#count plot
print(df["Job Role"].value_counts())

plt.figure(figsize=(10,5))

sns.countplot(
    y="Job Role",
    data=df,
    order=df["Job Role"].value_counts().index
)

plt.title("Job Role Distribution")
plt.show()

#overtime vs attrition
sns.countplot(x="Over Time", hue="Attrition", data=df)
plt.title("Over Time vs Attrition")
plt.show()


#Monthly Income
#box plot
plt.boxplot(
    df["Monthly Income"],
    notch=True,
    vert=True,
    patch_artist=True,
    widths=0.3,
    tick_labels=["Monthly Income"],
    showmeans=True,
    meanline=True,
    whis=1.5,
    boxprops=dict(linewidth=2, color="red"),
    medianprops=dict(linewidth=3, color="green"),
    whiskerprops=dict(linewidth=2)
)

plt.ylabel("Income")
plt.title("Monthly Income Distribution")
plt.show()


#stem plot
#Employee Age Distribution:
age_count = df["Age"].value_counts().sort_index()

plt.stem(
    age_count.index,
    age_count.values,
    linefmt="r--",
    markerfmt="*g",
    basefmt="--"
)

plt.xlabel("Employee Age")
plt.ylabel("Employee Count")
plt.title("Age Distribution Stem Plot")
plt.show()

#corrlation heatmap
numeric_df = df.select_dtypes(include="number")
print(numeric_df.corr())

plt.figure(figsize=(12,8))
sns.heatmap(numeric_df.corr(), cmap="coolwarm")
plt.title("Correlation Heatmap")



plt.show()

# ==========================
# Business Insights
# ==========================

print("\n===== Business Insights =====")
print(f"Total Employees : {len(df)}")
print(f"Average Monthly Income : {df['Monthly Income'].mean():.2f}")
print(f"Highest Salary : {df['Monthly Income'].max()}")
print(f"Lowest Salary : {df['Monthly Income'].min()}")
print(f"Attrition Rate : {(df['Attrition']=='Yes').mean()*100:.2f}%")