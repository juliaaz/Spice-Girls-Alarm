import csv
import random

with open('word-meaning-examples.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    num = random.randint(0, 13160)
    data = {}
    for row in csv_reader:
        data[row["Word"]] = [row["Meaning"]]
        examples = [row[example] for example in ["Examples/0", "Examples/1",
                                                 "Examples/2", "Examples/3",
                                                 "Examples/4", "Examples/5",
                                                 "Examples/6", "Examples/7",
                                                 "Examples/8", "Examples/9"] if
                    row[example] != ""]
        data[row["Word"]].append(examples)
    print(data[random.choice(list(data.keys()))])
