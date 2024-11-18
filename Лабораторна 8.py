
# Основний словник для зберігання інформації про групу
academic_performance = {
    "group_number": "КНд-35с",  # Номер групи
    "course": 1,  # Курс
    "students": {  # Словник студентів, де ключ - ПІБ студента
        "Гордієнко Іван Іванович": {
            "subjects": {
                "Математика": [90, 85, 88],
                "Фізика": [92, 80, 86],
                "Програмування": [95, 93, 97]
            }
        },
        "Петренко Захар Денисович": {
            "subjects": {
                "Математика": [75, 80, 78],
                "Фізика": [82, 85, 79],
                "Програмування": [88, 84, 90]
            }
        },
        "Коваленко Олександр Олександрович": {
            "subjects": {
                "Математика": [85, 88, 82],
                "Фізика": [80, 85, 84],
                "Програмування": [92, 91, 89]
            }
        },
        "Шевченко Тетяна Михайлівна": {
            "subjects": {
                "Математика": [95, 90, 92],
                "Фізика": [89, 87, 90],
                "Програмування": [96, 95, 97]
            }
        }
    }
}

# Функція 1: Додавання нового студента
def add_student(group_dict, full_name, subjects):
   
    if full_name in group_dict["students"]:
        print(f"Студент {full_name} вже існує у групі {group_dict['group_number']}.")
    else:
        group_dict["students"][full_name] = {
            "subjects": subjects
        }
        print(f"Студента {full_name} додано до групи {group_dict['group_number']}.")

# Функція 2: Пошук студента за ім'ям
def find_student(group_dict, full_name):
  
    student = group_dict["students"].get(full_name)
    if student:
        return student
    else:
        return f"Студента {full_name} не знайдено у групі {group_dict['group_number']}."

# Демонстрація роботи функцій
print("\n=== Додавання нового студента ===")
add_student(academic_performance, "Коваленко Денис Сергійович", {
    "Математика": [85, 87, 89],
    "Фізика": [83, 88, 90],
    "Програмування": [92, 90, 93]
})

print("\n=== Пошук студента ===")
print(find_student(academic_performance, "Кравченко Віталій Вікторович"))
