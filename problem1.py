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

def find_in_table(table, name):
    """Ищет песни артиста по имени и выдаёт про него информацию

    Параметры:
    table -- основная таблица
    name -- имя артиста
    """
    songs = []
    for row in table:
        if row["artist_name"] == name:
           songs.append(row)
    return songs

def write_table(table, name):
    """Создаёт таблицу со столбцами track_name, streams, date для одного артиста

    Параметры:
    table -- основная таблица
    name -- имя артиста
    """
    artist_rows = [list(x.values()) for x in find_in_table(table, name)]

    with open("songs_artst.csv", "w", encoding="utf8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["track_name", "streams", "date"])
        writer.writerows(artist_rows)


if __name__ == "__main__":
    name = input("Введите имя исполнителя: ")
    table = read_table("songs.txt")
    if find_in_table(table, name):
        write_table(table, name)
        print("Результат записан в файл songs_artst.csv")
    else:
        print("Такого исполнителя не удалось найти.")