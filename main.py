#1-misol
nums = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

print(result)

#2-misol
words = ["python", "java", "javascript", "c"]

longest = max(words, key=lambda x: len(x))

print(longest)

#3-misol
students = {
    "Ali": 85,
    "Vali": 92,
    "Sami": 78,
    "Zara": 95
}

sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

print(sorted_students)

#4-misol
data = [(1, 5, 2), (10, 3, 7), (4, 9, 6)]

result = list(map(lambda x: max(x), data))

print(result)

#5-misol
a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x, y: x + y, a, b))

print(result)
