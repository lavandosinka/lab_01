class Firma:
    def __init__(self, name: str, price: float, mass: float):
        self.name = name
        self.price = price
        self.mass = mass

    def get_price(self):
        return self.price

    def set_price(self, value):
        if value <= 0:
            print("Стоимость должна быть больше 0")
        else:
            self.price = value

    def get_mass(self):
        return self.mass

    def set_mass(self, value):
        if value <= 0:
            print("Масса должна быть больше 0")
        else:
            self.mass = value

    def total_cost(self):
        if self.price <= 0 or self.mass <= 0:
            print("Неверные данные")
            return 0
        else:
            return self.price * self.mass


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Значение должно быть больше 0. Попробуйте снова.")
        except ValueError:
            print("Введите числовое значение. Попробуйте снова.")

def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()  # Убираем пробелы с начала и конца строки
        if value:
            return value
        else:
            print("Имя не может быть пустым. Попробуйте снова.")

def menu():
    objects = []

    while True:
        print("\nМеню:")
        print("1. Создать объект")
        print("2. Установить цену")
        print("3. Установить массу")
        print("4. Вычислить общую стоимость")
        print("5. Показать данные объекта")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = get_non_empty_string("Введите имя объекта: ")
            price = get_positive_float("Введите цену объекта: ")
            mass = get_positive_float("Введите массу объекта: ")
            obj = Firma(name, price, mass)
            objects.append(obj)
            print(f"Объект {name} создан.")

        elif choice == "2":
            idx = int(input("Введите индекс объекта (начиная с 0): "))
            if 0 <= idx < len(objects):
                new_price = get_positive_float("Введите новую цену: ")
                objects[idx].set_price(new_price)
            else:
                print("Неверный индекс.")

        elif choice == "3":
            idx = int(input("Введите индекс объекта (начиная с 0): "))
            if 0 <= idx < len(objects):
                new_mass = get_positive_float("Введите новую массу: ")
                objects[idx].set_mass(new_mass)
            else:
                print("Неверный индекс.")

        elif choice == "4":
            idx = int(input("Введите индекс объекта (начиная с 0): "))
            if 0 <= idx < len(objects):
                total = objects[idx].total_cost()
                print(f"Общая стоимость объекта: {total}")
            else:
                print("Неверный индекс.")

        elif choice == "5":
            idx = int(input("Введите индекс объекта (начиная с 0): "))
            if 0 <= idx < len(objects):
                obj = objects[idx]
                print(f"Объект: {obj.name}, Цена: {obj.price}, Масса: {obj.mass}")
            else:
                print("Неверный индекс.")

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


# Запуск меню
menu()
