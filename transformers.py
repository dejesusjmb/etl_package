from config import INVALID_DATA


class Transformer:
    @staticmethod
    def transform(data):
        pass

    @staticmethod
    def to_exclude(data):
        return data in INVALID_DATA


class EngineLocationTransformer(Transformer):
    @staticmethod
    def transform(data):
        value_map = {'front': 1, 'rear': 0}
        return value_map[data]


class NumOfCylindersTransformer(Transformer):
    @staticmethod
    def transform(data):
        num_str_to_int = {
            'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
            'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
            'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20
        }
        return num_str_to_int[data]


class EngineSizeTransformer(Transformer):
    @staticmethod
    def transform(data):
        return int(data)


class WeightTransformer(Transformer):
    @staticmethod
    def transform(data):
        return int(data)


class HorsepowerTransformer(Transformer):
    @staticmethod
    def transform(data):
        return float(data.replace(',', '.'))


class AspirationTransformer(Transformer):
    @staticmethod
    def transform(data):
        return 1 if data == 'turbo' else 0


class PriceTransformer(Transformer):
    @staticmethod
    def transform(data):
        return float(data) / 100


class MakeTransformer(Transformer):
    @staticmethod
    def transform(data):
        return data
