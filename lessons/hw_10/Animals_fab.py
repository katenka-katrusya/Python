from Animals import Birds, Cats, Dogs, Fish


class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    @staticmethod
    def _get_maker(animal_type: str):
        types = {"bird": Birds, "cat": Cats, "dog": Dogs, "fish": Fish}
        return types[animal_type.lower()]


fabric = AnimalFabric()
animal_from_fabric = fabric.make_animal("dog", "Товарищ", 40, 4, "Дворняга", "Шерсть")
animal_from_fabric1 = fabric.make_animal("cat", "Пуговка", 2, 2, "Дворняга", "Шерсть")

print(animal_from_fabric)
print(animal_from_fabric1)
print(fabric.make_animal('bird', "Кеша", 1, 2, "Попугай", "Перья", "На абордааааж"))
print(fabric.make_animal('fish', "Ужас", 1, 1, "Пиранья", "Чешуя"))