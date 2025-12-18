# class firstClass:
#     x = 5
# print(firstClass.x)
# class fruit:
#     def getinfo(self):
#         print('This is a fruit class')
# object1 = fruit()
# object1.getinfo()
# class kalkulator:
#     def __init__(self, number1, number2):
#         self.number1 = number1
#         self.number2 = number2
#     def pertambahan(self):
#         hasil = self.number1 + self.number2
#         print(f"{self.number1} + {self.number2} = {hasil}")
#     def pengurangan(self):
#         hasil = self.number1 - self.number2
#         print(f"{self.number1} - {self.number2} = {hasil}")
#     def perkalian(self):
#         hasil = self.number1 * self.number2
#         print(f"{self.number1} * {self.number2} = {hasil}")
#     def pembagian(self):
#         hasil = self.number1 / self.number2
#         print(f"{self.number1} / {self.number2} = {hasil}")

# simplekalkulator = kalkulator(6,2)
# simplekalkulator.pertambahan()
# simplekalkulator.pengurangan()
# simplekalkulator.perkalian()
# simplekalkulator.pembagian()

#inheritance
class Person:
    def __init__(self, name, age, hairColor):
        self.name = name
        self.age = age
        self.hairColor = hairColor
    def eat(self):
        msg = str(self.name)+" can also eat"
        return msg
    def drink(self):
        msg = str(self.name)+" can also drink"
        return msg
class student(Person):
    def __init__(self, name, age, hairColor, nis):
        super().__init__(name, age, hairColor)
        self.nis = nis
    def parentName(self):
        msg = self.__class__.__base__
        return(msg.__name__)
    def study(self):
        className = __class__.__name__
        msg = "As a "+className.lower()+" "
        msg += self.name+" should  study"
        return(msg)
object1 = student("zaahid", 12, "Black", 567789)
print(object1.nis)
print(object1.study())
# parentClass = object1.parentName()
# print(object1.name, "inherits all thins from", parentClass)
# print(object1.__class__.__name__, "is technician class")
# print(object1.name, "is an object created from Person class")
# print(object1.eat())
# print(object1.drink())