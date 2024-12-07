import random


class Encryptor:
    def __init__(self, *numbers):

        self.__numbers = numbers

        self.__result = None

    def __random_operation(self):
        operations = ['+', '-', '*', '/']
        operation = random.choice(operations)
        result = self.__numbers[0]

        for num in self.__numbers[1:]:
            if operation == '+':
                result += num
            elif operation == '-':
                result -= num
            elif operation == '*':
                result *= num
            elif operation == '/' and num != 0:
                result /= num
            else:
                continue
        return result, operation

    def calculate(self):

        self.__result, operation = self.__random_operation()
        print(f"Використана операція: {operation}")

    def __str__(self):

        if self.__result is None:
            return "Результат ще не розрахований. Викличте метод calculate()."
        return f"Результат: {self.__result}"



encryptor = Encryptor(10, 20, 5)
print(encryptor)
encryptor.calculate()
print(encryptor)