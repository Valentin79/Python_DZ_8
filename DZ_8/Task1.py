# Напишите функцию, которая получает на вход директорию и
# рекурсивно обходит её и все вложенные директории. Результаты обхода
# сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте
# родительскую директорию. Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
# с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def dir_size(path) -> int: # Функция для подсчета размера директории со всем внутри.
    res = 0
    for dir_path, dir_name, file_name in os.walk(path):
        for j in file_name:
            p = f"{dir_path}\\{j}"
            res += os.path.getsize(p)
    return res


def dir_walk() -> dict: # обход директории и создания словаря (без параметра обходит текущую директорию)
    parent_dir = None
    result = {}
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        for i in dir_name:
            path = f"{dir_path}\\{i}" # формируем путь, что бы передать его функциям
            # ключ - директория или файл, значение - размер и родительская директория
            result[f"Директория: {i}"] = (f"Размер: {dir_size(path)}, р/д: {parent_dir}")
        for j in file_name:
            path = f"{dir_path}\\{j}"
            result[f"Файл: {j}"] = (f"Размер: {os.path.getsize(path)}, р/д: {parent_dir}")
        parent_dir = i # со следующего уровня - р.д - та, по которой мы только что прошли.
    return result


result = dir_walk()

with(
    open("json_file.json", "w", encoding="utf-8") as f_json,
    open("csv_file.csv", "w", newline='', encoding='utf-8') as f_csv,
    open("pickle_file.pickle", "wb") as f_pcl
):
    # запись в json
    json.dump(result, f_json, ensure_ascii=False, indent=4)
    f_json.write("\n")

    # запись в csv
    csv_writer = csv.writer(f_csv, dialect='excel', delimiter=' ')
    all_data = []
    for key, value in result.items():
        all_data = [key, value]
        csv_writer.writerow(all_data)

    # запись в pickle
    pickle.dump(result, f_pcl)




