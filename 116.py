# -----------------------------------
# DAY 17 - ALL IN ONE PANDAS BASICS
# -----------------------------------

import pandas as pd

print("\n--- PANDAS SERIES ---")
s = pd.Series([10, 20, 30, 40], index=['a','b','c','d'])
print(s)
print("Access:", s['b'])


print("\n--- DATAFRAME CREATION ---")
data = {
    "name": ["Om", "Raj", "Keya", "Neha"],
    "age": [20, 21, 20, 22],
    "marks": [85, 90, 88, 70]
}
df = pd.DataFrame(data)
print(df)


print("\n--- BASIC INFO ---")
print("Head:\n", df.head())
print("\nInfo:")
print(df.info())
print("\nDescribe:\n", df.describe())
print("\nShape:", df.shape)
print("Columns:", df.columns)


print("\n--- SELECTING COLUMNS ---")
print(df["name"])
print(df[["name", "marks"]])


print("\n--- SELECTING ROWS (loc & iloc) ---")
print("loc (row 0):\n", df.loc[0])
print("iloc (row 1):\n", df.iloc[1])
print("iloc rows 0-2, cols 0-2:\n", df.iloc[0:2, 0:2])


print("\n--- FILTERING ---")
print("Marks > 80:\n", df[df["marks"] > 80])
print("Marks > 80 & age < 22:\n", df[(df["marks"] > 80) & (df["age"] < 22)])


print("\n--- ADDING & DROPPING COLUMNS ---")
df["grade"] = ["A", "A+", "A", "B"]
print("Added grade:\n", df)

df = df.drop("age", axis=1)
print("\nAfter dropping age:\n", df)


print("\n--- RENAMING COLUMN ---")
df.rename(columns={"marks": "score"}, inplace=True)
print(df)


print("\n--- HANDLING MISSING VALUES ---")
df.loc[1, "score"] = None   # make one missing value
print("Missing added:\n", df)

print("Missing count:\n", df.isnull().sum())
df["score"].fillna(df["score"].mean(), inplace=True)
print("\nAfter fillna:\n", df)


print("\n--- SORTING ---")
print(df.sort_values("score", ascending=False))


print("\n--- GROUP BY (VERY IMPORTANT) ---")
# Add age column back for groupby example
df["age"] = [20, 21, 20, 22]

print("Group by age (avg score):\n", df.groupby("age")["score"].mean())
print("Group count:\n", df.groupby("age").size())


print("\n--- MINI ANALYSIS PROJECT ---")
print("Average Score:", df["score"].mean())
print("Students Score > 80:\n", df[df["score"] > 80])
print("Group by age (count):\n", df.groupby("age").count())

print("\n--- END OF DAY 17 CODE ---")
