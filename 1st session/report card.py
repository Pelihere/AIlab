scores = {
    "Ali": 18,
    "Sara": 20,
    "Reza": 9,
    "Mina": 14,
    "Omid": 11.5
}

passed_students = []

for name, score in scores.items():
    if score >= 17:
        grade = "عالی"
    elif score >= 14:
        grade = "خوب"
    elif score >= 10:
        grade = "قبول"
    else:
        grade = "مردود"

    print(f"{grade} -> {name}: {score}")

    if score >= 10:
        passed_students.append(name)

average = sum(scores.values()) / len(scores)
top_student = max(scores, key=scores.get)

print("قبول شده‌ها:", passed_students)
print("میانگین کلاس:", average)
print("نفر اول:", top_student)