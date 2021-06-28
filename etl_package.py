import csv

from config import ESSENTIAL_FIELDS_COLUMN
from transformers import (
    EngineLocationTransformer,
    NumOfCylindersTransformer,
    EngineSizeTransformer,
    WeightTransformer,
    HorsepowerTransformer,
    AspirationTransformer,
    PriceTransformer,
    MakeTransformer
)


class ETLPackage:
    data = None
    transformers = [
        EngineLocationTransformer,
        NumOfCylindersTransformer,
        EngineSizeTransformer,
        WeightTransformer,
        HorsepowerTransformer,
        AspirationTransformer,
        PriceTransformer,
        MakeTransformer
    ]

    @staticmethod
    def load(filename, delimiter=';'):
        data = []
        with open(filename, 'r') as file:
            for line in file:
                data.append(line.split(delimiter))
        ETLPackage.data = data

    @staticmethod
    def to_csv(filename, data):
        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    @staticmethod
    def transform():
        if not ETLPackage.data:
            raise Exception('No data is loaded.')

        filtered_data = ETLPackage.filter_columns(ETLPackage.data, ESSENTIAL_FIELDS_COLUMN.values())
        transformed_data = [list(filtered_data[0])]

        for line in filtered_data[1:]:
            transformed_line = list(line)
            for index, transformer in enumerate(ETLPackage.transformers):
                cell = line[index]
                if transformer.to_exclude(cell):
                    transformed_line = None
                    break
                transformed_line[index] = transformer.transform(cell)

            if transformed_line:
                transformed_data.append(transformed_line)

        return transformed_data

    @staticmethod
    def filter_columns(data, column_numbers):
        filtered_data = list(zip(*data))
        filtered_data = [filtered_data[index] for index in column_numbers]
        return list(zip(*filtered_data))
