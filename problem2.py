import csv

def get_row(row):
    """"Считывает строку и выдаёт обработанный словарь

    Параметры:
    row -- строка
    """
    return {"streams": int(row[0]), "artist_name": row[1], "track_name": row[2],"date": row[3]}

def read_table(filename):
    """Возвращает лист из словарей обработанной таблицы

    Параметры:
    filename -- имя файла
    """
    table = []
    header = True
    with open(filename, "r", encoding="utf8") as f:
        for row in csv.reader(f, delimiter="?"):
            if header:
                header = False
                continue
            table.append(get_row(row))
    return table

def bubble_sort(arr, key=lambda x: x):
    """"Сортирует массив алгоритмом пузырька

    Параметры:
    array -- массив
    key -- ключ сортировки
    """
    while True:
        swap = False
        for i in range(len(arr)-1):
            j = i+1
            if key(arr[i]) > key(arr[j]):
                arr[j], arr[i] = arr[i], arr[j]
                swap = True

        if not swap:
            break



if __name__ == "__main__":
    table = read_table("songs.txt")
    bubble_sort(table, key=lambda x: x["streams"])

    for i in range(1, 6):
        song = table[-i]
        print(f"{i} место: {song['track_name']}, {song['artist_name']}, {song['date']}.")