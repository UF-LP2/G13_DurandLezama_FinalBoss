""" declaracio Clases"""


class Ship:
    """ clase de barco"""
    numbarco = 0

    def __init__(self, draft, crew):
        Ship.numbarco += 1
        self.numbarco = Ship.numbarco
        self.draft = float(draft)
        self.crew = float(crew)

    def is_worth_it(self):
        """Function printing python version."""
        if (self.draft - self.crew*1.5) <= 20:
            raise ValueError("Error, no saquear")
        elif (self.draft - self.crew*1.5) > 20:
            return True


class Cargo(Ship):
    """Function printing python version."""

    def __init__(self, cargo, quality, draft, crew):
        self.cargo = float(cargo)
        self.quality = (quality)
        super().__init__(draft, crew)

    def checking_cargo(self):
        """ clase de cargo"""
        if self.cargo == "":
            self.cargo = 0

        if self.quality == 1:
            self.cargo = self.cargo+3, 5
        elif self.quality == 0.5:
            self.cargo = self.cargo+2
        elif self.quality == 0.25:
            self.cargo = self.cargo+0.5
        else:
            raise ValueError("Error, no hay cargo")

    def is_worth_it(self):
        self.checking_cargo()

        if (self.draft+self.cargo) - self.crew*1.5 <= 20:
            raise ValueError("Error, no saquear")
        elif (self.draft+self.cargo) - self.crew*1.5 > 20:
            return True


class Cruise(Ship):
    """ clase de crucero"""

    def __init__(self, passengers, draft, crew):
        self.passengers = float(passengers)
        super().__init__(draft, crew)

    def is_worth_it(self):

        if (self.draft - self.crew*1.5) - self.passengers <= 20:
            raise ValueError("Error, no saquear")
        elif (self.draft - self.crew*1.5) - self.passengers > 20:
            return True
