import math

# #ulesanna 1
# try:
#     a=float(input("Введите число: "))
#     if a > 0:
#         print("Число положительное.")
#         if a % 2 == 0:
#             print("Число четное.")
#         else:
#             print("Число нечетное.")
#     elif a < 0:
#         print("Число отрицательное.")
#     else:
#         print("Число равно нулю.")
# except ValueError:
#     print("Ошибка: введите корректное числовое значение.")

# #ulesanna 2
# try:
#     a=float(input("Введите угол 1: "))
#     b=float(input("Введите угол 2: "))
#     c=float(input("Введите угол 3: "))
#     print("Эти углы могут быть углами треугольника?")
#     if a > 0 and b > 0 and c > 0:
#         if a+b+c == 180:
#             if a == b == c:
#                 print("Да. Это равносторонний треугольник")
#             elif a == b or b == c or a == c:
#                 print("Да. Это равнобедренный треугольник")
#             else:
#                 print("Да. Это разносторонний треугольник")
#         else:
#             print("!!!Сумма углов не равна 180, это не треугольник")
#     else:
#         print("!!!Углы должны быть положительными числами")

# except ValueError:
#     print("!!!Ошибка")

# #ulesanna 3
# x=input("Хотите расшифровать порядковый номер дня недели? (да/нет): ").lower()
# if x == "да":
#     try:
#         y = int(input("Введите номер дня недели (от 1 до 7): "))
#         if 1 <= y <= 7:
#             s = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
#             print(f"День недели: {s[y- 1]}")
#         else:
#             print("Ошибка: введите число от 1 до 7.")
#     except ValueError:
#         print("Ошибка: введите корректное числовое значение.")
# else:
#     print("Вы выбрали не расшифровывать порядковый номер дня недели.")

# #ulesanna 4
# def zodiac_sign(day, month):
#     # Проверяем, что день и месяц в допустимом диапазоне
#     if month == 1:
#         return "Козерог" if day <= 19 else "Водолей"
#     elif month == 2:
#         return "Водолей" if day <= 18 else "Рыбы"
#     elif month == 3:
#         return "Рыбы" if day <= 20 else "Овен"
#     elif month == 4:
#         return "Овен" if day <= 20 else "Телец"
#     elif month == 5:
#         return "Телец" if day <= 21 else "Близнецы"
#     elif month == 6:
#         return "Близнецы" if day <= 20 else "Рак"
#     elif month == 7:
#         return "Рак" if day <= 22 else "Лев"
#     elif month == 8:
#         return "Лев" if day <= 22 else "Дева"
#     elif month == 9:
#         return "Дева" if day <= 22 else "Весы"
#     elif month == 10:
#         return "Весы" if day <= 22 else "Скорпион"
#     elif month == 11:
#         return "Скорпион" if day <= 21 else "Стрелец"
#     elif month == 12:
#         return "Стрелец" if day <= 21 else "Козерог"
#     else:
#         return "Неверный месяц"

# # Запрашиваем день и месяц рождения пользователя
# try:
#     day = int(input("Введите день рождения (от 1 до 31): "))
#     month = int(input("Введите месяц рождения (от 1 до 12): "))
    
#     # Проверяем, что день и месяц в допустимом диапазоне
#     if 1 <= day <= 31 and 1 <= month <= 12:
#         # Проверяем на корректность дней для каждого месяца
#         if (month == 2 and day > 29) or \
#            (month in [4, 6, 9, 11] and day > 30) or \
#            (month not in [2, 4, 6, 9, 11] and day > 31):
#             print("Ошибка: Неверное количество дней в этом месяце.")
#         else:
#             # Определяем знак зодиака
#             sign = zodiac_sign(day, month)
#             print(f"Ваш знак зодиака: {sign}")
#     else:
#         print("Ошибка: Неверные значения дня или месяца.")
# except ValueError:
#     print("Ошибка: Пожалуйста, введите корректные числовые значения для дня и месяца.")

# #ulesanna 5
# q = input("Введите число или текст: ")

# if q.isdigit() or (q.replace('.', '', 1).isdigit() and q.count('.') < 2): #проверяем ли это число
#     n = float(q)

#     if n.is_integer(): #целое ли число
#         result = n * 0.5  #если целое, находим 50%
#         print(f"Число {n} целое. 50% от него: {result}")
#     else:
#         result = n * 0.7  #если дробное, находим 70%
#         print(f"Число {n} дробное. 70% от него: {result}")
# else:
#     print(f"Введенный текст: {q}") #если это текст

# #ulesanna 6

# h = input("Хотите решить квадратное уравнение? (да/нет): ").lower()

# if h == "да":
#     a = float(input("Введите коэффициент a: "))
#     b = float(input("Введите коэффициент b: "))
#     c = float(input("Введите коэффициент c: "))

#     D = b**2 - 4*a*c #Дискриминант
#     if D > 0:
#         # Если D > 0, два решения
#         x1 = (-b + math.sqrt(D)) / (2 * a)
#         x2 = (-b - math.sqrt(D)) / (2 * a)
#         print(f"Два решения: x1 = {x1:.2f}, x2 = {x2:.2f}")
#     elif D == 0:
#         # Если D = 0, одно решение
#         x = -b / (2 * a)
#         print(f"Одно решение: x = {x:.2f}")
#     else:
#         # Если D < 0, нет решений
#         print("Решений нет.")
# else:
#     print("До свидания!")