# Homework_2.py

class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession
    
    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет, я работаю {self.profession}")


class Classmate(Person):
    def __init__(self, name, age, profession, group_name):
        super().__init__(name, age, profession)
        self.group_name = group_name
    
    def introduce(self):
        print(f"Привет! Я {self.name}, мне {self.age} лет. Я учусь в группе {self.group_name} и хочу стать {self.profession}")


class Friend(Person):
    def __init__(self, name, age, profession, hobby):
        super().__init__(name, age, profession)
        self.hobby = hobby
    
    def introduce(self):
        print(f"Привет! Я {self.name}, мне {self.age} лет. По профессии я {self.profession}, а в свободное время люблю заниматься {self.hobby}")


# Создаем объекты Classmate
classmate1 = Classmate("Алексей", 20, "программистом", "ПИ-21")
classmate2 = Classmate("Мария", 19, "дизайнером", "ДЗ-20")

# Создаем объекты Friend
friend1 = Friend("Иван", 25, "инженер", "фотографией")
friend2 = Friend("Ольга", 23, "маркетолог", "йогой")

# Вызываем метод introduce() у каждого объекта
print("=== Одногруппники ===")
classmate1.introduce()
classmate2.introduce()

print("\n=== Друзья ===")
friend1.introduce()
friend2.introduce()
