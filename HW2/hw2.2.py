user_name = input("Введите свое имя: ")

correct_answers = 0
points_quantity = 0

print(f"Привет, {user_name}, начинаем тренировку!")

first_question = input("Введи пропущенное слово 'My name ___ Vova' : ")
if first_question == 'is':
    print('Ответ верный! Вы получаете 10 баллов!')
    correct_answers += 1
    points_quantity += 10
else:
    print(f"Неправильно. Правильный ответ: 'is'")


second_question = input("Введи пропущенное слово 'I ___ a coder.' : ")
if second_question == 'am':
    print('Ответ верный! Вы получаете 10 баллов!')
    correct_answers += 1
    points_quantity += 10
else:
    print(f"Неправильно. Правильный ответ: 'am'")


third_question = input("Введи пропущенное слово 'I live ___ Moscow.' : ")
if third_question == 'in':
    print('Ответ верный! Вы получаете 10 баллов!')
    correct_answers += 1
    points_quantity += 10
else:
    print(f"Неправильно. Правильный ответ: 'in'")


print(f'Вот и всё, {user_name}!')
print(f'Количество верных ответов: {correct_answers}')
print(f'Ваш счет: {points_quantity}')
print(f'Процент правильных ответов: {(correct_answers / 3) * 100}%')

