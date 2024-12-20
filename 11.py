class Тварина:
    def __init__(self, імя, вид, звук):
        self.імя = імя
        self.вид = вид
        self.звук = звук

    def видай_звук(self):
        return f"{self.імя} ({self.вид}) каже {self.звук}"

    def __str__(self):
        return f"{self.імя} - це {self.вид}."

class Собака(Тварина):
    def __init__(self, імя, порода):
        super().__init__(імя, "Собака", "Гав")
        self.порода = порода

    def принеси_мяч(self):
        return f"{self.імя} приносить мяч!"

    def __str__(self):
        return f"{self.імя} - це {self.порода} {self.вид}."

class Кіт(Тварина):
    def __init__(self, імя, колір):
        super().__init__(імя, "Кіт", "Мяу")
        self.колір = колір

    def дряпай(self):
        return f"{self.імя} дряпає меблі!"

    def __str__(self):
        return f"{self.імя} - це {self.колір} {self.вид}."

if __name__ == "__main__":
    собака = Собака("Рекс", "Золотистий ретрівер")
    кіт = Кіт("Мішель", "Чорний")

    print(собака)
    print(собака.видай_звук())
    print(собака.принеси_мяч())

    print(кіт)
    print(кіт.видай_звук())
    print(кіт.дряпай())