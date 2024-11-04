def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha() and char.lower() in letter_count:
            letter_count[char.lower()] += 1
        else:
            if char.isalpha():
                letter_count[char.lower()] = 1

    return letter_count


def calculate_frequency(letter_counts):
    total_chars = sum(letter_counts.values())
    frequencies = {letter: count / total_chars for letter, count in letter_counts.items()}

    return frequencies


# Пример использования функций
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
result_count = count_letters(main_str)
result_freq = calculate_frequency(result_count)

for letter, frequency in result_freq.items():
    print(f"{letter}: {frequency:.2%}")


