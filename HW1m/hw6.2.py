words_easy = { # словарь для уровня сложности "легкий"
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = { # словарь для уровня сложности "средний"
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = { # словарь для уровня сложности "сложный"
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = { # уровни, которые будет получать пользователь после решения задач
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}


def choose_difficulty(level):  # функция выбора сложности
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


def play_game(words):  # функция основной логики вопросов пользователю
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


def display_results(answers):  # функция вывода результатов пользователю
    right_answers = []
    wrong_answers = []
    for key, value in answers.items():
        if value:
            right_answers.append(key)
        else:
            wrong_answers.append(key)
    print("Правильно отвечены слова:")
    for true_answer in right_answers:
        print(true_answer)
    print("Неправильно отвечены слова:")
    for false_answer in wrong_answers:
        print(false_answer)


def calculate_rank(answers):  # функция возвращает ранг пользователя на основе его верных ответов
    correct_answers = 0
    for answer in answers:
        if answers[answer] == True:
            correct_answers += 1
    user_rank = levels[correct_answers]
    return f"Ваш ранг: \n{user_rank}"


words = choose_difficulty("легкий")
answers = play_game(words)
display_results(answers)
calculate_rank(answers)
