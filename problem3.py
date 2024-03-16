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


def find_song(table, song_name):
    """Ищет информацию про заданную песню в таблице

    Параметры:
    table -- основная таблица
    song_name -- название песни
    """
    for row in table:
        if row["track_name"] == song_name:
            return row

if __name__ == "__main__":
    table = read_table("songs.txt")
    while True:
        command = input("Введите название песни: ")
        if command == "0": break

        song = find_song(table, command)
        if song:
            print(f"Песня {song['track_name']} принадлежит {song['artist_name']}")
        else:
            print("К сожалению, ничего не удалось найти.")


