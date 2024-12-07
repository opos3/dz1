result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("Число 'a' меньше числа 'b'.")
        if b > 100:
            raise IndexError("Число 'b' більше 100.")
        return a / b
    except ZeroDivisionError:
        print(f"Помилка: Поділ на нуль при a={a}, b={b}.")
    except ValueError as ve:
        print(f"Помилка: {ve} при a={a}, b={b}.")
    except IndexError as ie:
        print(f"Помилка: {ie} при a={a}, b={b}.")
    except TypeError:
        print(f"Помилка: Неправильний тип даних при a={a}, b={b}.")
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(int(key), data[key])
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Необроблена помилка: {e} при обробці key={key}, value={data[key]}.")

print("Результат:", result)