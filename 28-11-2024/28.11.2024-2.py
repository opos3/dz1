from colorama import Fore, Back, Style, init


init()

print(Fore.RED + "Цей текст буде червоним")
print(Back.GREEN + "А цей текст на зеленому тлі")
print(Style.BRIGHT + "Цей текст яскравий" + Style.RESET_ALL)


print("Повернення до стандартного стилю")