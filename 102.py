with open("sample.txt", "r") as f:
    data = f.read()

characters = len(data)
words = len(data.split())
lines = len(data.split("\n"))

print("Characters:", characters)
print("Words:", words)
print("Lines:", lines)
