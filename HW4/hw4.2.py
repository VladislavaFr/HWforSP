user_name = input("Введите свое имя: ")

correct_answers = 0

questions = ['My name ___ Vova', 'I ___ a coder.', 'I live ___ Moscow.']
answers = ['is', 'am', 'in'] #список верных ответов

print(f"Привет, {user_name}. Предлагаю проверить свои знания английского!")
user_input_ready = input(f"Наберите 'ready', чтобы начать!")
if user_input_ready != "ready":
    print("Кажется, вы не хотите играть. Очень жаль.")

elif user_input_ready == "ready":
    for index, question in enumerate(questions): #для индексирования вопросов
        quest = input(f"Введи верный ответ: {question}: ")
        if quest == answers[index]: #для проверки ответов в списке при помощи срезов
            print("Ответ верный!")
            correct_answers += 1
        else:
            print(f"Неправильно. Правильный ответ: {answers[index]}")

answers = (correct_answers / 3) * 100
round_answers = round(answers, 2)

print(f'Вот и всё! Вы ответили на {correct_answers} вопросов из 3 верно, это {round_answers} процентов.')


