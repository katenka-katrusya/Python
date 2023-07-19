class Animals:

    def __init__(self, name: str, weight: int, age: int, body_cover: str):
        self.name = name
        self.weight = weight
        self.age = age
        self.body_cover = body_cover

    def area(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f"{self.name} {self.weight} {self.age} {self.body_cover}"


class Birds(Animals):
    def __init__(self, name: str, weight: int, age: int, body_cover: str, bird_type: str, sound: str):
        super().__init__(name, weight, age, body_cover)
        self.bird_type = bird_type
        self.sound = sound

    def area(self):
        return "Обитает в воздухе"

    def say(self):
        return self.sound

    def __str__(self):
        return f"{super().__str__()} {self.bird_type} {self.say()} {self.area()}"


class Cats(Animals):
    def __init__(self, name: str, weight: int, age: int, body_cover: str, cat_type: str):
        super().__init__(name, weight, age, body_cover)
        self.cat_type = cat_type

    def area(self):
        return "Ходит где хочет"

    def say(self):
        return "Мяу-мяу"

    def __str__(self):
        return f"{super().__str__()} {self.cat_type} {self.say()} {self.area()}"


class Dogs(Animals):
    def __init__(self, name: str, weight: int, age: int, body_cover: str, dog_type: str):
        super().__init__(name, weight, age, body_cover)
        self.dog_type = dog_type
        self.commands = []

    def area(self):
        return "Ходит по земле"

    def say(self):
        return "Гав-гав"

    def __str__(self):
        return f"{super().__str__()} {self.dog_type} {self.say()} {self.area()}"


class Fish(Animals):
    def __init__(self, name: str, weight: int, age: int, body_cover: str, fish_type: str):
        super().__init__(name, weight, age, body_cover)
        self.fish_type = fish_type

    def area(self):
        return "Обитает в воде"

    def say(self):
        return "Буль-буль"

    def __str__(self):
        return f"{super().__str__()} {self.fish_type} {self.say()} {self.area()}"


cat = Cats("Матильда", 3, 3, "Британка", "Шерсть")
dog = Dogs("Шарик", 35, 7, "Дворняга", "Шерсть")
bird = Birds("Иннокентий", 1, 2, "Ворона", "Перья", "Каррр")
fish = Fish("Василий", 7, 3, "Щука", "Чешуя")

print(cat)
print(dog)
print(bird)
print(fish)