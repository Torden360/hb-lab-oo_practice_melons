############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, name, is_bestseller = None):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []


    def add_pairing(self, *pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


# def make_melon_types(code, name, first_harvest, color, is_seedless, pairing, is_bestseller):
#     """Returns a list of current melon types."""

#     all_melon_types = []

#     code = MelonType(code, first_harvest, color, is_seedless, is_bestseller, name)

#     pairing = (code, pairing)

#     code.add_pairing(pairing)

#     all_melon_types.append(code)

#     return all_melon_types

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # instantiating class
    melon_musk = MelonType('musk', '1998', 'green', True, 'Muskmelon', True)
    melon_musk.add_pairing('mint')

    melon_casaba = MelonType('cas', '2003', 'orange', False, 'Casaba')
    melon_casaba.add_pairing('mint', 'strawberries')

    melon_crenshaw = MelonType('cren', '1996', 'green', False, 'Crenshaw')
    melon_crenshaw.add_pairing('proscuitto')

    melon_yellow_watermelon = MelonType('yw', '2013', 'yellow', False, 'Yellow Watermelon', True)
    melon_yellow_watermelon.add_pairing('ice cream')

    all_melon_types.append(melon_musk)
    all_melon_types.append(melon_casaba)
    all_melon_types.append(melon_crenshaw)
    all_melon_types.append(melon_yellow_watermelon)

    return all_melon_types

melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with {melon.pairings}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for i, melon in enumerate(melon_types):
        melon_dict[melon.code] = melon_types[i]

    return melon_dict
    
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



