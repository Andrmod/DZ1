import time


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.energy = 100
        self.hunger = 0
        self.mood = 100
        self.sleepy = False

    def eat(self):
        if self.hunger > 50:
            self.hunger -= 50
            self.energy += 20
            self.mood += 10
            print(f"{self.name} поїв! Енергія +20, настрій +10.")
        else:
            print(f"{self.name} не голодний!")

    def play(self):
        if self.energy > 30:
            self.energy -= 30
            self.mood += 20
            print(f"{self.name} грає! Настрій +20, енергія -30.")
        else:
            print(f"{self.name} занадто втомлений для гри.")

    def sleep(self):
        if self.energy < 100:
            self.energy = 100
            self.mood += 10
            self.hunger += 20
            print(f"{self.name} спить! Енергія відновлена, настрій +10.")
            self.sleepy = False
        else:
            print(f"{self.name} не хоче спати, він вже повністю відпочив!")

    def walk(self):
        if self.energy > 20:
            self.energy -= 20
            self.hunger += 30
            self.mood += 10
            print(f"{self.name} гуляє! На вулиці! Енергія -20, голод +30, настрій +10.")
        else:
            print(f"{self.name} занадто втомлений для прогулянки.")

    def status(self):
        print(f"Статус собачки {self.name}:")
        print(f"Енергія: {self.energy}")
        print(f"Голод: {self.hunger}")
        print(f"Настрій: {self.mood}")
        print(f"Хоче спати: {'Так' if self.sleepy else 'Ні'}")

    def time_passes(self):
        self.hunger += 10
        self.mood -= 5
        if self.energy < 50:
            self.sleepy = True
        print(f"Час проходить... Голод +10, настрій -5.")
        self.status()



dog = Dog("Бобі", "Коргі")


dog.status()
dog.eat()
dog.play()
dog.walk()
dog.time_passes()
dog.sleep()
dog.time_passes()