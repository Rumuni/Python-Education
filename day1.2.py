students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

total_score = 0

for student in students:
    print(student["name"], "さんの点数は", student["score"], "点です")
    total_score += student["score"]

average = total_score / len(students)
print("平均点は", average, "点です")