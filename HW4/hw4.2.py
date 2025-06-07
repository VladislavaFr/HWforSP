user_name = input("Введите свое имя: ")

correct_answers = 0

questions = ['My name ___ Vova', 'I ___ a coder.', 'I live ___ Moscow.']
answers = ['is', 'am', 'in']

print(f"Привет, {user_name}. Предлагаю проверить свои знания английского!")
user_input_ready = input(f"Наберите 'ready', чтобы начать!")
if user_input_ready != "ready":
    print("Кажется, вы не хотите играть. Очень жаль.")

elif user_input_ready == "ready":
    first_question = input(f"Введи верный ответ: {questions[0]}: ")
    if first_question == answers[0]:
        print("Ответ верный!")
        correct_answers += 1
    else:
        print(f"Неправильно. Правильный ответ: {answers[0]}")


    second_question = input(f"Введи верный ответ: {questions[1]}: ")
    if second_question == answers[1]:
        print("Ответ верный!")
        correct_answers += 1
    else:
        print(f"Неправильно. Правильный ответ: {answers[1]}")


    third_question = input(f"Введи верный ответ: {questions[2]}: ")
    if third_question == answers[2]:
        print("Ответ верный!")
        correct_answers += 1
    else:
        print(f"Неправильно. Правильный ответ: {answers[2]}")

    print(f'Вот и всё! Вы ответили на {correct_answers} вопросов из 3 верно, это {(correct_answers / 3) * 100} процентов.')


