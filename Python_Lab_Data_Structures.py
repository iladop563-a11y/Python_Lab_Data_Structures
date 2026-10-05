import timeit

print("========== ЗАВДАННЯ 1 ==========")

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("Початковий список:", numbers)
print("Елемент за індексом 2:", numbers[2])
print("Елемент за індексом -1:", numbers[-1])

print("Зріз [1:5]:", numbers[1:5])
print("Зріз [:4]:", numbers[:4])
print("Зріз [::2]:", numbers[::2])

numbers.append(90)
print("Після append(90):", numbers)

numbers.insert(2, 25)
print("Після insert(2, 25):", numbers)

numbers.remove(50)
print("Після remove(50):", numbers)


print("\n========== ЗАВДАННЯ 2 ==========")

students = [
    ("Кузін", "БІКСБ-2-25-4-Од", [90, 85, 88]),
    ("Іваненко", "БІКСБ-2-25-4-Од", [75, 82, 79]),
    ("Петренко", "БІКСБ-2-25-4-Од", [95, 91, 93])
]

def unpack_student(student):
    surname, group, grades = student
    return surname, group, grades

def average_grade(students):
    all_grades = []
    for surname, group, grades in students:
        all_grades.extend(grades)
    return sum(all_grades) / len(all_grades)

for student in students:
    surname, group, grades = unpack_student(student)
    print(surname, "|", group, "|", grades)

print("Середній бал:", round(average_grade(students), 2))

try:
    students[0][0] = "Нове прізвище"
except TypeError as error:
    print("Помилка зміни кортежу:", error)

student = ("Кузін", [90, 85, 88])
print("Кортеж до зміни вкладеного списку:", student)

student[1].append(100)
print("Кортеж після зміни вкладеного списку:", student)


print("\n========== ЗАВДАННЯ 3 ==========")

text = """
Python є популярною мовою програмування.
Python використовується для навчання.
Програмування на Python є зручним.
"""

normalized_text = text.lower()

for symbol in ".,!?;:":
    normalized_text = normalized_text.replace(symbol, "")

words = normalized_text.split()

frequencies = {}

for word in words:
    frequencies[word] = frequencies.get(word, 0) + 1

print("Частоти слів за алфавітом:")

for word in sorted(frequencies):
    print(word, ":", frequencies[word])

print("Частоти за спаданням:")

for word, count in sorted(
    frequencies.items(),
    key=lambda item: (-item[1], item[0])
):
    print(word, ":", count)

filtered = {
    word: count
    for word, count in frequencies.items()
    if count >= 2
}

print("Слова з частотою не менше 2:", filtered)
print("Частота відсутнього слова:", frequencies.get("java", 0))


print("\n========== ЗАВДАННЯ 4 ==========")

collection_a = [1, 2, 2, 3, 4, 5, 5]
collection_b = [4, 5, 5, 6, 7, 8]
collection_c = [1, 2]

set_a = set(collection_a)
set_b = set(collection_b)
set_c = set(collection_c)

print("Множина A:", sorted(set_a))
print("Множина B:", sorted(set_b))
print("Множина C:", sorted(set_c))

print("Перетин A і B:", sorted(set_a & set_b))
print("Об'єднання A і B:", sorted(set_a | set_b))
print("Симетрична різниця A і B:", sorted(set_a ^ set_b))

print("C є підмножиною A:", set_c <= set_a)
print("B є підмножиною A:", set_b <= set_a)


print("\n========== ЗАВДАННЯ 5 ==========")

sizes = [100, 1000, 10000]
repeats = 5

print(
    f"{'n':<10}"
    f"{'List, мс':<15}"
    f"{'Set, мс':<15}"
    f"{'Dict, мс':<15}"
    f"{'Unique list, мс':<20}"
    f"{'Unique set, мс':<20}"
)

for n in sizes:
    data = list(range(n))
    data_set = set(data)
    data_dict = {x: x for x in data}
    target = n - 1

    list_time = timeit.timeit(
        lambda: target in data,
        number=repeats
    ) / repeats * 1000

    set_time = timeit.timeit(
        lambda: target in data_set,
        number=repeats
    ) / repeats * 1000

    dict_time = timeit.timeit(
        lambda: target in data_dict,
        number=repeats
    ) / repeats * 1000

    def unique_list():
        result = []
        for value in data:
            if value not in result:
                result.append(value)
        return result

    def unique_set():
        result = set()
        for value in data:
            result.add(value)
        return result

    unique_list_time = timeit.timeit(
        unique_list,
        number=repeats
    ) / repeats * 1000

    unique_set_time = timeit.timeit(
        unique_set,
        number=repeats
    ) / repeats * 1000

    print(
        f"{n:<10}"
        f"{list_time:<15.6f}"
        f"{set_time:<15.6f}"
        f"{dict_time:<15.6f}"
        f"{unique_list_time:<20.6f}"
        f"{unique_set_time:<20.6f}"
    )

print("\nВисновки:")
print("Пошук у списку має складність O(n).")
print("Пошук у множині в середньому має складність O(1).")
print("Пошук ключа у словнику в середньому має складність O(1).")
print("Накопичення унікальних значень у списку може наближатися до O(n^2).")
print("Накопичення унікальних значень у множині в середньому має O(n).")
print("Для частих звернень за ключем доцільно використовувати словник.")
print("Для швидкої перевірки повторів доцільно використовувати множину.")
print("Для збереження порядку без дублікатів можна поєднати список і множину.")