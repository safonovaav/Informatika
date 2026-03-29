# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # открывваем файл для чтения
    with open(INPUT_FILENAME, 'r') as input_f:
        # читаем файл csv как словарь
        r = csv.DictReader(input_f)
        # создаем список
        x = list(r)
    # открываем файл для записи
    with open(OUTPUT_FILENAME, 'w') as output_f:
        json.dump(x, output_f, indent=4) # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
