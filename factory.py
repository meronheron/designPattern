from abc import ABC, abstractmethod
#creational design pattern
# abstract Product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
# concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
class AnimalFactory:# factory
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")
def main():
    # create factory
    factory = AnimalFactory()  
    # create animals using factory
    dog = factory.create_animal("dog")
    cat = factory.create_animal("cat")   
    # test the products
    print(dog.speak())  # Output: Woof!
    print(cat.speak())  # Output: Meow!

if __name__ == "__main__":
    main()