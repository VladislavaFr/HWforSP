words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard   = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}


levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}


def choose_difficulty(level): #функция выбора сложности уровня
    words = {}
    level_selection = input("Выберите уровень сложности (легкий / средний / сложный): ").lower()
    if level_selection == "легкий" or "лёгкий":
        words = words_easy
    elif level_selection == "средний":
        words = words_medium
    elif level_selection == "сложный":
        words = words_hard
    else:
        words = words_medium
    return words


def play_game(words): #функция для самой игры
    answers = {}
    for key, value in words.items():
        suggested_word = input(f"{key}, {len(value)} букв, начинается на {value[0]}...").lower()
        if suggested_word == value:
            print(f"Верно. {key} — это {value}.")
            answers[key] = True
        else:
            print(f"Неверно. {key} — это {value}.")
            answers[key] = False
    return answers


def display_results(answers): #считает правильные и неправильные ответы
    true_ans = []
    false_ans = []
    for key, value in answers.items():
        if value:
            true_ans.append(key)
        else:
            false_ans.append(key)
    print("Правильно отвечены слова:")
    for true_answer in true_ans:
        print(true_answer)
    print("Неправильно отвечены слова:")
    for false_answer in false_ans:
        print(false_answer)


def calculate_rank(answers): #ранг пользователя
    range_of_user = 0
    for answer in answers:
        if answers[answer] == True:
            range_of_user += 1
    name_of_range = levels[range_of_user]
    print(f"Ваш ранг: \n{name_of_range}")


words = choose_difficulty("легкий")
answers = play_game(words)
display_results(answers)
calculate_rank(answers)
