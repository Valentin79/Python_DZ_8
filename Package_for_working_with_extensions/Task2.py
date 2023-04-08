# 📌 Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в
# JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json


def get_user_info(json_file: str) -> None:
    used_ids = set()
    levels = set(range(1,8))
    users = {}

    with open(json_file, "r", encoding="utf-8") as f:
        users = json.load(f)

    for _, val in users.items():
        for name, id in val.items():
            used_ids.add(id)

    while True:
        user_name, user_id, user_level = input(
            "Введите через пробел имя, идентификатор, уровень доступа > "
        ).split()
        user_id = int(user_id)
        if user_name == "":
            break
        while user_id in used_ids:
            print("Пользователь с таким id уже существует")
            user_name, user_id, user_level = input(
                "Введите через пробел имя, идентификатор, уровень доступа > "
            ).split()
        else:
            used_ids.add(id)

        user_level = int(user_level)
        while user_level not in levels:
            print(f"Уровень доступа {user_level} не существует")
            user_name, user_id, user_level = input(
                "Введите через пробел имя, идентификатор, уровень доступа > "
            ).split()

        users.setdefault(user_level, {})[user_name] = user_id
        print(users)
        with open(json_file, "w", encoding="utf-8") as f_json:
            json.dump(users, f_json, ensure_ascii=False)


get_user_info("file1.json")
