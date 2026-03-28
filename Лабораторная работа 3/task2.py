# TODO Напишите функцию find_common_participants
# Функция, принимающая участников и разделитель
def find_common_participants(group_1,group_2,a=','):
    # Для каждой строки создали списки; создали общий список
    list1 = group_1.split(a)
    list2 = group_2.split(a)
    b = []
    # Перебираем имена: сначала первую группу, затем смотрим есть ли человек из списка 2 в списке b. Если нет, добавляем
    for name in list1:
        if name in list2 and name not in b:
            b.append(name)
# Сортируем по алфавиту
    return sorted(b)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group)

print(result)