# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Петя"},
]
# spis=[]

# for i in students: - в лоб, если известны Имена учеников и их кол-во для вывода
#     spis.append(i['first_name'])
# print(spis)

# print(f"Вася: {spis.count("Вася")}")
# print(f"Петя: {spis.count("Петя")}")
# print(f"Маша: {spis.count("Маша")}")

spis = []
spis_no_repit = []

for i in students:  # Преобразование к списку
    spis.append(i["first_name"])

# spis_no_repit=set(spis)  - через множества не получилось красиво вывести
# print(spis_no_repit)

for i in spis:  # присваиваем переменной список без повторов
    if i not in spis_no_repit:
        spis_no_repit.append(i)

for i in range(len(spis_no_repit)):
    print(f"{spis_no_repit[i]}: {spis.count(spis_no_repit[i])}")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Оля"},
]

spis, spis_no_repit = [], []
resul_num, resul_name = 0, str

for i in students:  # Преобразование к списку
    spis.append(i["first_name"])

for i in spis:  # присваиваем переменной список без повторов
    if i not in spis_no_repit:
        spis_no_repit.append(i)

for i in range(len(spis_no_repit)):  # Цикл по вычислению кол-во повторов
    povtor = spis.count(
        spis_no_repit[i]
    )  # узнаем кол-во повторов и записываем в переменную
    if povtor > resul_num:
        resul_num, resul_name = povtor, spis_no_repit[i]
print("Самое частое имя среди учеников:", resul_name)
print("Повторений:", resul_num)

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {"first_name": "Вася"},
        {"first_name": "Вася"},
    ],
    [  # это – второй класс
        {"first_name": "Маша"},
        {"first_name": "Маша"},
        {"first_name": "Оля"},
    ],
    [  # это – третий класс
        {"first_name": "Женя"},
        {"first_name": "Петя"},
        {"first_name": "Женя"},
        {"first_name": "Саша"},
    ],
]
for j in school_students:  # Выбираем каждый класс, обнуляя все вычисления
    schet1, resul_num, resul_name = 0, 0, str
    spis, spis_no_repit = [], []

    for i in j:  # Преобразование к списку
        spis.append(i["first_name"])

    for i in spis:  # присваиваем переменной список без повторов
        if i not in spis_no_repit:
            spis_no_repit.append(i)

    for i in range(len(spis_no_repit)):  # Цикл по вычислению кол-во повторов
        povtor = spis.count(
            spis_no_repit[i]
        )  # узнаем кол-во повторов и записываем в переменную
        if povtor > resul_num:
            resul_num, resul_name = povtor, spis_no_repit[i]
    print("Самое частое имя среди учеников:", resul_name)
    print("Повторений:", resul_num)


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "2б", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
    {
        "class": "2в",
        "students": [
            {"first_name": "Даша"},
            {"first_name": "Олег"},
            {"first_name": "Маша"},
        ],
    },
]
is_male = {
    "Олег": True,
    "Маша": False,
    "Оля": False,
    "Миша": True,
    "Даша": False,
}
for i in school:
    spis = []
    male, female = 0, 0
    for j in i["students"]:  # Преобразовываем к списку именя в выбранном словаре i
        spis.append(j["first_name"])
    for j in range(len(spis)):  # Перебираем каждое имя
        if (
            is_male[spis[j]] == True
        ):  # Сравниваем имя с буливым значением в словаре сравнения
            male += 1
        else:
            female += 1
    print(f"Класс {i["class"]}: девочки - {female}, мальчики - {male}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "3c", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
]
is_male = {
    "Маша": False,
    "Оля": False,
    "Олег": True,
    "Миша": True,
}
res_male, res_female = 0, 0
for i in school:
    spis = []
    male, female = 0, 0
    for j in i["students"]:  # Преобразовываем к списку именя в выбранном словаре i
        spis.append(j["first_name"])
    for j in range(len(spis)):  # Перебираем каждое имя
        if (
            is_male[spis[j]] == True
        ):  # Сравниваем имя с буливыми значением в словаре сравнения
            male += 1
        else:
            female += 1
    if (
        male > res_male
    ):  # Сравниваем парней, где начальное кол-во равно 0 и присваеваем, если больше
        res_male = male
        res_class_male = i["class"]

    if (
        female > res_female
    ):  # Сравниваем девочек, где начальное кол-во равно 0, так же присваеваем, если больше
        res_female = female
        res_class_female = i["class"]
print(f"Больше всего мальчиков в классе - {res_class_male}, мальчиков - {res_male}")
print(f"Больше всего девочек в классе - {res_class_female}, девочек - {res_female}")
