import json
import csv


def reader(json_name: str) -> dict[str, str, str]:
    with open(json_name, 'r', encoding='utf-8') as f_in:
        new_dct = json.load(f_in)
    return new_dct


def write_to_csv(users_dct: dict, csv_name: str) -> None:
    users_data = [[i_lvl, u_id, u_nm]
                  for i_lvl, i_usr in users_dct.items()
                  for u_id, u_nm in i_usr.items()]
    with open(csv_name, 'w', encoding='utf-8') as f_out:
        csv_writer = csv.writer(f_out, dialect='excel', delimiter=';')
        csv_writer.writerows(users_data)


def main():
    write_to_csv(reader('file1.json'), 'index.csv')


if __name__ == '__main__':
    main()
