import csv
import random

def generating_data():
    """Reading and generating necessary data about random word."""
    with open('word-meaning-examples.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        num = random.randint(0, 13160)
        data = {}
        for row in csv_reader:
            data[row["Word"]] = [row["Meaning"]]
            examples = [row[example] for example in
                        ["Examples/0", "Examples/1",
                         "Examples/2", "Examples/3",
                         "Examples/4", "Examples/5",
                         "Examples/6", "Examples/7",
                         "Examples/8", "Examples/9"] if
                        row[example] != ""]
            data[row["Word"]].append(examples)
    key = random.choice(list(data.keys()))
    data = data[key]
    return [key] + data

def quize_definitions():
    """Definition quize generation."""
    data_1 = generating_data()
    word_correct = data_1[0]
    words = [generating_data()[0], generating_data()[0], word_correct]
    words = random.sample(words, len(words))
    words_str = '| '
    for word in words:
        words_str += word + ' | '
    print('\nPrint the correct word for this definition:' + f'\n"{data_1[1]}"')
    print(f"\nChoose among: {words_str}")
    word_input = str(input("\nYour answer: "))
    if word_input == word_correct:
        print("Good job!")
        return True
    else:
        print("It's wrong word :(")
        print(f"Correct answer: {word_correct}\n")
        return False

def quize_exampes():
    """Example quize generation."""
    data_1 = generating_data()
    word_correct = data_1[0]
    words = [generating_data()[0], generating_data()[0], word_correct]
    words = random.sample(words, len(words))
    words_str = '| '
    for word in words:
        words_str += word + ' | '
    sentence = random.choice(data_1[2]).lower().replace(word_correct.lower(),
                                                        '_________').capitalize()
    print('\nPut in the correct word into the sentence:' + f'\n"{sentence}"')
    print(f"\nChoose among: {words_str}")
    word_input = str(input("\nYour answer: "))
    if word_input == word_correct:
        print("Good job!")
        return True
    else:
        print("It's wrong word :(")
        print(f"\nCorrect answer: {word_correct}\n")
        return False

def choosing_quiz():
    """Choosing one of quizes in random way."""
    num = random.randint(0,1)
    if num == 0:
        return quize_exampes()
    else:
        return quize_definitions()

def generating_quiz():
    """Generating the whole quize process."""
    for _ in range(3):
        res = choosing_quiz()
        if res == False:
            return False
    return True
