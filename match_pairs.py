def match_pairs(boys, girls):
    # Проверяем, что количество юношей и девушек одинаково
    if len(boys) != len(girls):
        print("Внимание, кто-то может остаться без пары.")
        return
    
    # Сортируем оба списка по алфавиту
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)

    # Выводим идеальные пары
    print("Идеальные пары:")
    for boy, girl in zip(boys_sorted, girls_sorted):
        print(f"{boy} и {girl}")

# Пример 1
boys1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls1 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
print(f"Пример 1:")
match_pairs(boys1, girls1)

# Пример 2
boys2 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
print(f"\n\nПример 2:")
match_pairs(boys2, girls2)