# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод init(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
#
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод init(), внутри которого будет вызываться родительский метод init(). В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.
import string
class Alphabet:
    def __init__(self, leng, letters):
        self.leng = leng
        self.letters = letters

    def print(self):
        print(self.letters)
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __lettersNum = 26

    def __init__(self):
        super().__init__("En", string.ascii_letters)
    def is_en_letter(self, letter):
        return letter.upper() in self.letters
    def letters_num(self):
        return EngAlphabet.__lettersNum
    @staticmethod
    def example():
        print("hi")

eng_alf = EngAlphabet()
eng_alf.print()
print(eng_alf.letters_num())
print(EngAlphabet.example())
print(eng_alf.is_en_letter("Щ"))








