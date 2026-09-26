import pandas as pd
import numpy as np

# =========================
# 1. LOAD DATA
# =========================

OUTPUT_FILE = "cleaned_student_data.csv"

df = pd.read_csv("data.csv")

print("Original Shape:", df.shape)


# =========================
# 2. BASIC INFORMATION
# =========================

print("\n--- Data Information ---")
print(df.info())

print("\n--- Missing Values ---")
print(df.isnull().sum())


# =========================
# 3. REMOVE DUPLICATES
# =========================

duplicate_count = df.duplicated().sum()

print("\nDuplicate Rows:", duplicate_count)

df = df.drop_duplicates()


# =========================
# 4. CLEAN CATEGORICAL DATA
# =========================

# Remove extra spaces
df["Gender"] = df["Gender"].str.strip().str.title()
df["Branch"] = df["Branch"].str.strip().str.upper()
df["City"] = df["City"].str.strip().str.title()
df["Placement_Status"] = df["Placement_Status"].str.strip().str.title()


# =========================
# 5. HANDLE MISSING VALUES
# =========================

# Numerical columns → median
numeric_columns = [
    "Age",
    "Semester",
    "Attendance_Percent",
    "Study_Hours_Per_Day",
    "Assignments_Completed",
    "Midterm_Score",
    "Final_Score",
    "Backlogs"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())


# Categorical columns → mode
categorical_columns = [
    "Gender",
    "Branch",
    "City",
    "Placement_Status"
]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])


# =========================
# 6. HANDLE INVALID VALUES
# =========================

# Attendance should be between 0 and 100
df["Attendance_Percent"] = df["Attendance_Percent"].clip(0, 100)

# Scores should be between 0 and 100
df["Midterm_Score"] = df["Midterm_Score"].clip(0, 100)
df["Final_Score"] = df["Final_Score"].clip(0, 100)

# Study hours should be realistic
df["Study_Hours_Per_Day"] = df["Study_Hours_Per_Day"].clip(0, 12)

# Backlogs cannot be negative
df["Backlogs"] = df["Backlogs"].clip(lower=0)


# =========================
# 7. CREATE NEW FEATURES
# =========================

# Average academic score
df["Average_Score"] = (
    df["Midterm_Score"] + df["Final_Score"]
) / 2

df["Average_Score"] = df["Average_Score"].round(2)


# Performance category
def performance_category(score):

    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Average"
    else:
        return "Poor"


df["Performance_Category"] = df["Average_Score"].apply(
    performance_category
)


# =========================
# 8. SORT DATA
# =========================

df = df.sort_values(
    by="Average_Score",
    ascending=False
)


# =========================
# 9. FINAL CHECK
# =========================

print("\n--- Cleaned Data ---")
print("Final Shape:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nFirst 5 Cleaned Records:")
print(df.head())


# =========================
# 10. SAVE CLEANED DATA
# =========================

df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaning completed successfully!")
print("Saved as:", OUTPUT_FILE)