import json


def load_data():
    with open("data/font.json", "r") as file:
        data = json.load(file)

    return data


def write_tab_name(tab_name):
    if tab_name not in get_tab_names():
        with open("data/tab_names.txt", "a") as file:
            file.write(tab_name + "\n")


def get_tab_names():
    with open("data/tab_names.txt", "r") as file:
        tab_names = file.readlines()

    return tab_names


def delete_tab_name(tab_name):
    tab_names = get_tab_names()
    if f"{tab_name}\n" in tab_names:
        # Entfernen des gewünschten Namens aus der Liste
        tab_names.remove(f"{tab_name}\n")

        # Schreiben der aktualisierten Liste zurück in die Datei
        with open("data/tab_names.txt", "w") as file:
            for name in tab_names:
                file.write(name)


def get_output_data(filename):
    with open(filename, "r") as file:
        data = file.read()

    return data
