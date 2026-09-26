import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_student_data.csv")

print("===== STUDENT PERFORMANCE ANALYSIS =====")

# Total students
print("\nTotal Students:", len(df))

# Average scores
print("Average Midterm Score:",
      round(df["Midterm_Score"].mean(), 2))

print("Average Final Score:",
      round(df["Final_Score"].mean(), 2))

print("Average Overall Score:",
      round(df["Average_Score"].mean(), 2))

# Highest and lowest
print("\nHighest Final Score:",
      df["Final_Score"].max())

print("Lowest Final Score:",
      df["Final_Score"].min())

# Attendance
print("\nAverage Attendance:",
      round(df["Attendance_Percent"].mean(), 2), "%")

# Study hours
print("Average Study Hours:",
      round(df["Study_Hours_Per_Day"].mean(), 2),
      "hours/day")

# Performance categories
print("\n===== PERFORMANCE CATEGORY =====")
print(df["Performance_Category"].value_counts())

# Branch analysis
print("\n===== BRANCH ANALYSIS =====")
print(df["Branch"].value_counts())




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD CLEANED DATA
# =========================

df = pd.read_csv("cleaned_student_data.csv")


# =========================
# CREATE DASHBOARD
# =========================

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

fig.suptitle(
    "Student Performance Analysis Dashboard",
    fontsize=22,
    fontweight="bold"
)


# =========================
# 1. STUDY HOURS VS FINAL SCORE
# =========================

axes[0, 0].scatter(
    df["Study_Hours_Per_Day"],
    df["Final_Score"],
    alpha=0.6
)

axes[0, 0].set_title("Study Hours vs Final Score", fontsize=13)
axes[0, 0].set_xlabel("Study Hours / Day")
axes[0, 0].set_ylabel("Final Score")
axes[0, 0].grid(True, alpha=0.3)


# =========================
# 2. ATTENDANCE VS FINAL SCORE
# =========================

axes[0, 1].scatter(
    df["Attendance_Percent"],
    df["Final_Score"],
    alpha=0.6
)

axes[0, 1].set_title("Attendance vs Final Score", fontsize=13)
axes[0, 1].set_xlabel("Attendance (%)")
axes[0, 1].set_ylabel("Final Score")
axes[0, 1].grid(True, alpha=0.3)


# =========================
# 3. PERFORMANCE CATEGORY
# =========================

performance = df["Performance_Category"].value_counts()

axes[0, 2].bar(
    performance.index,
    performance.values
)

axes[0, 2].set_title("Performance Category", fontsize=13)
axes[0, 2].set_xlabel("Performance")
axes[0, 2].set_ylabel("Number of Students")

for i, value in enumerate(performance.values):
    axes[0, 2].text(
        i,
        value + 5,
        str(value),
        ha="center",
        fontweight="bold"
    )


# =========================
# 4. BRANCH-WISE STUDENTS
# =========================

branch = df["Branch"].value_counts()

axes[1, 0].bar(
    branch.index,
    branch.values
)

axes[1, 0].set_title("Branch-wise Students", fontsize=13)
axes[1, 0].set_xlabel("Branch")
axes[1, 0].set_ylabel("Number of Students")

for i, value in enumerate(branch.values):
    axes[1, 0].text(
        i,
        value + 5,
        str(value),
        ha="center",
        fontweight="bold"
    )


# =========================
# 5. MIDTERM VS FINAL SCORE
# =========================

axes[1, 1].scatter(
    df["Midterm_Score"],
    df["Final_Score"],
    alpha=0.6
)

axes[1, 1].set_title("Midterm vs Final Score", fontsize=13)
axes[1, 1].set_xlabel("Midterm Score")
axes[1, 1].set_ylabel("Final Score")
axes[1, 1].grid(True, alpha=0.3)


# =========================
# 6. CORRELATION HEATMAP
# =========================

columns = [
    "Attendance_Percent",
    "Study_Hours_Per_Day",
    "Assignments_Completed",
    "Midterm_Score",
    "Final_Score",
    "Backlogs"
]

correlation = df[columns].corr()

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    ax=axes[1, 2],
    cbar=False
)

axes[1, 2].set_title("Correlation Heatmap", fontsize=13)


# =========================
# FINAL ADJUSTMENTS
# =========================

plt.subplots_adjust(
    top=0.88,
    bottom=0.08,
    left=0.06,
    right=0.98,
    hspace=0.35,
    wspace=0.25
)


# =========================
# SAVE GRAPH
# =========================

plt.savefig(
    "student_performance_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nGraph saved as: student_performance_analysis.png")

plt.show()