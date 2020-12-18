import pandas, numpy
from yargy                  import Parser
from yargy.interpretation   import fact

from Rules.City             import CityRule         as CityFilter
from Rules.Street           import StreetRule       as StreetFilter
from Rules.Building         import BuildingRule     as BuildingFilter
from Rules.Appartment       import AppartmentRule   as AppartmentFilter

class Address:
    def __init__(self):
        self.city = (None, None)
        self.street = (None, None)
        self.building = (None, None, None)
        self.appartment = None

    def print(self):
        print(self.city)
        print(self.street)
        print(self.building)
        print(self.appartment)

class AddressNERHypothesis:
    def predict(self, input):
        address = Address()
        
        # Parse cities
        matches = list(Parser(CityFilter).findall(input))
        if (len(matches)):
            Fact = matches[0].fact
            address.city = (Fact.title, Fact.prefix)

        # Parse streets
        matches = list(Parser(StreetFilter).findall(input))
        if (len(matches)):
            Fact = matches[0].fact
            address.street = (Fact.title, Fact.prefix)

        # Parse buildings
        matches = list(Parser(BuildingFilter).findall(input))
        if (len(matches)):
            Fact = matches[0].fact
            address.building = (Fact.house, Fact.corpus, Fact.structure)

        # Parse appartments
        matches = list(Parser(AppartmentFilter).findall(input))
        if (len(matches)):
            Fact = matches[0].fact
            address.appartment = Fact.appartment

        return address
