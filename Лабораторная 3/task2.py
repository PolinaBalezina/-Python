# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(group1, group2):
    group1_list = group1.split("|")
    group2_list = group2.split("|")
    common_elements = set(group1_list).intersection(set(group2_list))
    result = "|".join(common_elements)
    return result
result = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", result)