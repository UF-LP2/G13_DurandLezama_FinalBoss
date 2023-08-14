"""Module providingFunction printing python version."""

import csv
from src.cFinalBoss import Cargo
from src.cFinalBoss import Ship
from src.cFinalBoss import Cruise

def main() -> None:
  """Function printing python version."""
  barcos=[]
  with open("src/ships.csv",'read') as file:
    reader=csv.reader(file)
    for row in reader:
      draft=float(row['cargo'])
      crew=float(row['crew'])
      extra=float(row['extra'])
      quality=float(row['quality'])
      
      if quality=="" and extra=="":
        ship_obj=Ship(draft,crew)
        barcos.append(ship_obj)
      elif quality !="":
        cargo_obj=Cargo(extra,quality,draft,crew)
        barcos.append(cargo_obj)
      elif quality =="":
        crusero_obj=Cruise(extra,draft,crew)
        barcos.append(crusero_obj)
  
  for i in barcos:
    try:
      i.is_worth_it()
    except ValueError as error:
      print(error)

if __name__ == "__main__":
  main()
