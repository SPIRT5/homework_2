def check_word():
    word = input("Введите слово, состоящее только из латинских букв: ")

    # Проверяем, состоит ли слово только из латинских букв (больших и маленьких)
    if word.isalpha() and all('a' <= c <= 'z' or 'A' <= c <= 'Z' for c in word):
        length = len(word)
        
        # Если количество букв чётное
        if length % 2 == 0:
            middle1 = word[length // 2 - 1]
            middle2 = word[length // 2]
            print(f"Результат: {middle1 + middle2}")
        
        # Если количество букв нечётное
        else:
            middle = word[length // 2]
            print(f"Результат: {middle}")
    else:
        print("Ошибка: введённое слово должно содержать только латинские буквы.")

# Запуск программы
check_word()