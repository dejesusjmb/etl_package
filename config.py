from collections import OrderedDict

ESSENTIAL_FIELDS_COLUMN = OrderedDict({
    'engine-location': 8,
    'num-of-cylinders': 19,
    'engine-size': 9,
    'weight': 24,
    'horsepower': 15,
    'aspiration': 1,
    'price': 22,
    'make': 17,
})

INVALID_DATA = {'- ', '-', ' -', None}
