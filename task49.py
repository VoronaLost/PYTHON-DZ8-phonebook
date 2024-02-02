import shutil
import os

def list_input(title):
    return input(f"Заполните графу {title} для текущей записи: ")

def phonebook_import(file_name = "phonebook.txt"):
    list1 = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    record = list(map(lambda x: list_input(x), list1))
    string_record = "~".join(record) + "\n"
    with open(file_name, "a", encoding="utf-8") as f:
        f.writelines(string_record)
    print("______\nЗапись добавлена, ", end = "")
    show_inf(2)

def check_file():
    try:
        with open("phonebook.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) == 0: 
                print("Справочник пуст, заполните его, либо загрузите готовый справочник")
                show_inf(2)
                return []
            else:
                return lines
    except FileNotFoundError:
        print("Справочник отстутсвует, занесите в него данные, либо загрузите готовый справочник")
        show_inf(2)
        return []

def check_input(buttons):
    button = "q"
    while button not in buttons:
        button = input(f"Для выбора введите {buttons[0]}-{buttons[-1]} : ")
        print("_____")
        if button not in buttons:
            print("Неверное значение. ", end ="")
    return button

def show_inf(option):
    message1 = "Переход в главное меню"
    message2 = "для продолжения нажмите Enter\n"
    if option == 1: input(f"{message1}, {message2}")
    elif option == 2: input(f"{message2}")

def download_phonebook():
    path =os.getcwd()
    shutil.copyfile(path + "\\sample.txt", path +"\\phonebook.txt")
    print("________\nСправочник загружен, ", end = "")
    show_inf(2)

def display_phonebook():
    count = 0
    my_lines = check_file()
    if len(my_lines) > 0:
        for i in my_lines:
            count+=1
            print(f"{count}. ", *(i.split("~")), end = "")
        print("\n________")
        show_inf(1)

def show_search():
    search_menu = "выберите поле для поиска:\n1 - Фамилия\n2 - Имя\n\
3 - Отчество\n4 - Номер телефона\n5 - Отмена, возврат в главное меню"
    menu_button = "0"
    button_list = ["1", "2", "3", "4", "5"]
    button_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    my_lines = check_file()
    find_list = []
    count = 0
    if len(my_lines) > 0:
        if menu_button !="5":
            print(f"{search_menu}\n______")
            menu_button = check_input(button_list)
            if menu_button != "5":
                search_i = input(f"Введите поисковой запрос (будет найдено любое совпадение по полю '{button_names[int(menu_button) - 1]}'): ").lower()
                print("_______\nРезультат поиска: ")
                for i in my_lines:
                    if search_i in i.split("~")[int(menu_button) - 1].lower():
                        count+= 1
                        print(f"{count}. ", *(i.split("~")), end = "")
                        find_list.append(i)
                if len(find_list) == 0: 
                    print("По запросу ничего не найденно")
                    return[1]
                return find_list
            else: return [0]
    return [0]

def repeat_empty_search(rep_or_skip):
    if rep_or_skip == 1:
        print("________\n1 - Выполнить новый поиск\n2 - Вернуться в главное меню")
        other_search = check_input(["1", "2"])
        if other_search == "2": 
            return 0
        else:
            return 1
    elif rep_or_skip == 0: return 0
    else: return 2

def search_phonebook():
    check_1 = show_search()
    if check_1[0] != 0: check_1[0] = 1
    repeat_or_not = repeat_empty_search(check_1[0])
    if repeat_or_not == 0:
        show_inf(1)
    else: 
        show_inf(2)
        search_phonebook()

def delete_record():
    print("Для удаления ", end = "")
    delete_list = list.copy(show_search())
    select = repeat_empty_search(delete_list[0])
    del_button = "1"
    if select == 0:
        show_inf(1)
    elif select == 1:
        show_inf(2)
        delete_record()
    else:
        while del_button =="1" and len(delete_list) != 0 :
            choose_list = [str(x) for x in range(1, len(delete_list) + 2)]
            print(f"______\nВыберите номер записи для удаления ({choose_list[0]}-{choose_list[-2]}). Для отмены операции нажмите {choose_list[-1]}")
            index = int(check_input(choose_list)) - 1
            if index != len(delete_list):
                with open("phonebook.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    info_delete = lines.pop(lines.index(delete_list[index]))
                    delete_list.pop(index)
                with open("phonebook.txt", "w", encoding="utf-8") as f:
                    f.writelines(lines)
                    print(*(info_delete.split("~")), "\nЗапись была успешно удалена") 
            print("1 - Удалить другую найденную запись\n2 - Выполнить новый поисковой запрос для удаления\n3 - Возврат в главное меню\n______")
            del_button = check_input(["1", "2", "3"])
            if del_button == "1" and len(delete_list) > 0:
                count = 0
                for i in delete_list:
                        count+= 1
                        print(f"{count}. ", *(i.split("~")), end = "")
            if len(delete_list) == 0: 
                input("Не осталось записей для удаления, возврат в главное меню. Для продолжения нажмите Enter")
                return None
        if del_button == "2": delete_record()

def change_record():
    print("Для изменения ", end = "")
    change_list = list.copy(show_search())
    select = repeat_empty_search(change_list[0])
    change_button = "1"
    list1 = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    if select == 0:
        show_inf(1)
        return None
    if select == 1:
        show_inf(2)
        change_record()
        return None
    while change_button =="1":
        choose_list = [str(x) for x in range(1, len(change_list) + 2)]
        print(f"\n\nВыберите номер записи для изменения ({choose_list[0]}-{choose_list[-2]}). Для отмены операции нажмите {choose_list[-1]}\n______")
        index = int(check_input(choose_list)) - 1
        if index == len(change_list):
            show_inf(1)
            return None
        else:
            info_change = change_list[index]
            print("Изменяемая запись:\n", *info_change.split("~"))
            print("Выберите поле для изменения\n1 - Фамилия\n2 - Имя\n3 - Отчество\n4 - Номер телефона\n5 - Изменить все поля\n6 - Отмена операции\n_________")
            field_index = int(check_input(["1", "2", "3", "4", "5", "6"]))
            if field_index in range(1, 5):
                mod_record = change_list[index].split("~")
                mod_record[field_index - 1] = input(f"Введите новую графу '{list1[field_index - 1]}' для текущей записи: ")
                change_list[index] = "~".join(mod_record)
            elif field_index == 5:
                change_list[index] = "~".join(list(map(lambda x: list_input(x), list1))) + "\n"
            if field_index != 6:
                with open("phonebook.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    change_index = lines.index(info_change)
                    lines.pop(change_index)
                    lines.insert(change_index, change_list[index])
                with open("phonebook.txt", "w", encoding="utf-8") as f:
                    f.writelines(lines)
                    print("______\n  Запись:")
                    print(*info_change.split("~"))
                    print("  была успешно изменена на:")
                    print(*change_list[index].split("~"))

            print("\n1 - Изменить другую запись по текущему запросу\n2 - Выполнить новый поисковой запрос для изменения\n3 - Возврат в главное меню\n______")
            change_button = check_input(["1", "2", "3"])
            if change_button == "1":
                count = 0
                for i in change_list:
                        count+= 1
                        print(f"{count}. ", *(i.split("~")), end = "")
    if change_button == "2": change_record()   
            
def main():
    button = "0"
    button_list = ["1", "2", "3", "4", "5", "6", "7"]
    menu = "Выберите один из вариантов:\n1 - Занести данные в справочник\n2 - Загрузить готовый справочник\n\
3 - Просмотреть данные из справочника\n4 - Выполнить поиск по полю справочника\n5 - Удалить запись из справочника\n\
6 - Изменить данные в справочнике\n7 - Завершить работу\n______"
    while button != "7":
        print(f"_____\n{menu}")
        button = check_input(button_list)
        if button == "1": phonebook_import()
        elif button == "2": download_phonebook()
        elif button == "3": display_phonebook()
        elif button == "4": search_phonebook()
        elif button == "5": delete_record()
        elif button == "6": change_record()
    print("Конец работы")    
if __name__ == '__main__':
    main()

