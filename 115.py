import pandas as pd

data = {
    "name": ["Om", "Raj", "Keya", "Neha"],
    "age": [20, 21, 20, 22],
    "marks": [85, 90, 88, 70]
}

df = pd.DataFrame(data)

print("DATA:\n", df)
print("\nAverage marks:", df["marks"].mean())
print("\nStudents with marks > 80:\n", df[df["marks"] > 80])
print("\nGroup by age:", df.groupby("age")["marks"].mean())
