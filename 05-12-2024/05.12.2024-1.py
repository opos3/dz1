import re

def calculator_decorator(func):
    def wrapper(expression):
        try:

            if not re.match(r'^[\d+\-*/(). ]+$', expression):
                raise ValueError("Вираз містить неприпустимі символи.")

            result = func(expression)
            print(f"Результат: {result}")
            return result
        except ZeroDivisionError:
            print("Помилка: Поділ на нуль.")
        except SyntaxError:
            print("Помилка: Синтаксична помилка у виразі.")
        except ValueError as ve:
            print(f"Ошибка: {ve}")
        except Exception as e:
            print(f"Невідома помилка: {e}")
        return None
    return wrapper

@calculator_decorator
def calculate(expression):
    return eval(expression)


calculate("10 + 20 / 2")
calculate("10 + (5 - 3) * 4")
calculate("10 / 0")
calculate("10 + 20 & 2")
calculate("10 + ")