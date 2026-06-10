import json
import os

# Файл атауы
FILE_NAME = "students.json"

def load_data():
    """Файлдан студенттер мәліметін оқу"""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_data(students):
    """Студенттер мәліметін файлға сақтау"""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)

def add_student(students):
    """Жаңа студент қосу және енгізуді тексеру"""
    print("\n--- Жаңа студент қосу ---")
    
    # Атын тексеру (бос болмауы керек)
    while True:
        name = input("Аты: ").strip()
        if name:
            break
        print("Қате: Студенттің аты бос болмауы керек!")

    # Жасын тексеру (оң сан болуы керек)
    while True:
        try:
            age = int(input("Жасы: "))
            if age > 0:
                break
            print("Қате: Жасы теріс мән немесе 0 болмауы керек!")
        except ValueError:
            print("Қате: Жасты санмен енгізіңіз!")

    # Бағасын тексеру (0-100 аралығы)
    while True:
        try:
            grade = float(input("Бағасы: "))
            if 0 <= grade <= 100:
                break
            print("Қате: Баға 0–100 аралығында болуы керек!")
        except ValueError:
            print("Қате: Бағаны санмен енгізіңіз!")

    # Студентті тізімге қосу және файлға сақтау
    new_student = {"name": name, "age": age, "grade": grade}
    students.append(new_student)
    save_data(students)
    print("Студент сәтті қосылды!")

def show_students(students):
    """Студенттер тізімін көрсету"""
    print("\n===== Студенттер тізімі =====")
    if not students:
        print("База бос. Студенттер табылмады.")
        return
    
    for idx, student in enumerate(students, 1):
        print(f"{idx}. Аты: {student['name']}, Жасы: {student['age']}, Бағасы: {student['grade']}")

def show_statistics(students):
    """Статистика мен талдау шығару"""
    print("\n===== Статистика =====")
    total_students = len(students)
    
    if total_students == 0:
        print("Статистика есептеу үшін базада студенттер болуы керек.")
        return

    # Студенттер саны
    print(f"Студенттер саны: {total_students}")

    # Орташа бағаны есептеу
    total_grades = sum(student['grade'] for student in students)
    average_grade = total_grades / total_students
    print(f"Орташа баға: {average_grade:.1f}")

    # Ең жоғары баға алған студентті табу
    top_student = max(students, key=lambda x: x['grade'])
    print(f"Ең жоғары баға: {top_student['name']} - {top_student['grade']}")

def main():
    """Бағдарламаның негізгі мәзірі (Меню)"""
    students = load_data()
    
    while True:
        print("\n===== Студенттер базасы =====")
        print("1. Студент қосу")
        print("2. Студенттер тізімін көру")
        print("3. Статистика")
        print("0. Шығу")
        
        choice = input("Таңдауыңыз: ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            show_statistics(students)
        elif choice == "0":
            print("Бағдарлама аяқталды. Сау болыңыз!")
            break
        else:
            print("Қате: Мұндай мәзір жоқ, қайтадан таңдаңыз.")

if __name__ == "__main__":
    main()
 #   if __name__ == "__main__":
 #   main()