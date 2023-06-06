import json

phone_number = {}
persons = []

file_bd = "C:/Users/mrfal/OneDrive/Рабочий стол/Study/PB.json"


def save():
    with open(file_bd, "w", encoding="utf-8") as data:
        data.write(json.dumps(phone_number, ensure_ascii=False))
    print("Список контактов успешно сохранены в файле PB.json")


def load():
    with open(file_bd, "r", encoding="utf-8") as data:
        phone_number = json.load(data)
    return phone_number


def print_2d_list(array):
    for i in range(len(array)):
        print(''.join(map(str, array[i])))


com_list = ["/menu - список всех комманд",
            "1 - общий список контактов",
            "2 - добавить телефон",
            "3 - добавить ФИО",
            "4 - удалить контакт",
            "5 - сохранить изменения",
            "6 - загрузить базу контактов",
            "7 - завершение программы"]

print('"Телефонная книга"')
run = True
while run:
    print("Доступные команды:")
    print_2d_list(com_list)
    command = input("Введите команду: ")
    if command == "1":
        print("Текущий список контактов:")
        if len(phone_number) == 0:
            print("Список контактов пуст")
        else:
            for key, value in phone_number.items():
                print(f"Телефон: {key}: {value}")
    elif command == "2":
        name = input('Введите телефон: ')
        if name in phone_number:
            print("Taкой телефон уже есть в книге")
        else:
            phone_number[name] = []
            print('Телефон успешно добавлен!')
    elif command == "3":
        print("Выберете номер телефона, для которого хотите добавить данные: ")
        name = input("Номер телефона: ")
        if name in phone_number:
            person_name = input("Введите данные (ФИО): ")
            phone_number[name] = [person_name]
            print('Данные успешно добавлены!')
        else:
            print("Такого телефона в книге нет!")
    elif command == "4":
        print("Вы действительно хотите удалить телефон?")
        answer = input("Ведите да или нет: ").lower()
        print(answer)
        if answer == "да":
            del_num = input('Введите номер телефона: ')
            if del_num in phone_number:
                del phone_number[del_num]
                print(f"Контакт с номером {del_num} удален")
        else:
            print("Такого номера нет в книге!")
    elif command == "5":
        save()
        print("Изменения успешно сохранены!")
    elif command == "6":
        phone_number = load()
        print('Книга контактов успешно загружена!')
    elif command == "7":
        save()
        print("Программа завершила свою роботу.")
        run = False
    elif command == "help":
        print_2d_list(com_list)
    else:
        print("Неопознная команда. Используйте справку help")
