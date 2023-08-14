"""Module providingFunction printing python version."""

import csv
from src.cFinalBoss import Cargo
from src.cFinalBoss import Ship
from src.cFinalBoss import Cruise


def main() -> None:
    """Function printing python version."""
    barcos = []
    with open("src/ship.csv") as file:
        reader = csv.reader(file, delimiter=',')
        next(file, None)

        for row in reader:
            draft = row[0]
            crew = row[1]
            extra = row[2]
            quality = row[3]

            if quality == "" and extra == "":
                ship_obj = Ship(draft, crew)
                barcos.append(ship_obj)

            elif quality != "":
                if extra == "":
                    extra = 0

                cargo_obj = Cargo(extra, quality, draft, crew)
                barcos.append(cargo_obj)
            elif quality == "":
                crusero_obj = Cruise(extra, draft, crew)
                barcos.append(crusero_obj)

    for i in barcos:
        try:
            flag = i.is_worth_it()
            if flag:
                print("saquear")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
