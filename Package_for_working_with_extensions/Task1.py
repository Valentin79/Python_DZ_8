# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.
import json


def names_json(txt_file: str, json_file: str) -> None:
    with(
        open(txt_file, "r", encoding="utf8") as f_txt,
        open(json_file, "w", encoding="utf-8") as f_json
    ):
        all_data = {}
        while data := f_txt.readline():
            name, number = data[:-1].split()
            number = int(number) if number.find(".") == -1 else float(number)
            all_data[name.capitalize()] = number
        json.dump(all_data, f_json, ensure_ascii=False, indent=4)


names_json("file3.txt", "j_file.json")