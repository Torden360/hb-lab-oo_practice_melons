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

        self.pairings.extend(pairing)


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

    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict
    
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shaping_rating, color_rating, field, name):
        # initializing
        self.melon_type = melon_type
        self.shaping_rating = shaping_rating
        self.color_rating = color_rating
        self.field = field
        self.name = name

    # @property
    # def is_sellable(self):
    #     return (self.shaping_rating > 5
    #             and self.color_rating > 5
    #             and self.field != 3
    #             )

    @property
    def is_sellable(self):
        if (self.shaping_rating > 5
                and self.color_rating > 5
                and self.field != 3
                ):
            return "(CAN BE SOLD)"
        else:
            return "(NOT SELLABLE)"


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    Melons = []

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'],8,7,2,'Sheila')
    melon_2 = Melon(melons_by_id['yw'],3,4,2,'Sheila')
    melon_3 = Melon(melons_by_id['yw'],9,8,3,'Sheila')
    melon_4 = Melon(melons_by_id['cas'],10,6,35,'Sheila')
    melon_5 = Melon(melons_by_id['cren'],8,9,35,'Michael')
    melon_6 = Melon(melons_by_id['cren'],8,2,35,'Michael')
    melon_7 = Melon(melons_by_id['cren'],2,3,4,'Michael')
    melon_8 = Melon(melons_by_id['musk'],6,7,4,'Michael')
    melon_9 = Melon(melons_by_id['yw'],7,10,3,'Sheila')

    Melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7,
        melon_8, melon_9])

    return Melons

melons = make_melons(melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
 
    for melon in melons:

        print(f"Harvested by {melon.name} from Field {melon.field} {melon.is_sellable}")



