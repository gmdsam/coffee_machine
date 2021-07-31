from src.ingredients import InitializeIngredients
from src.beverages import BeverageFactory
import json


if __name__ == '__main__':
    # Reading test data
    with open('./data/input1.json') as file:
        data = json.load(file)

    # Initialize predefined ingredients with quantity given in input
    InitializeIngredients(data['machine']['total_items_quantity'])

    # Loop over each beverage available in input for preparation
    for beverage, composition in data['machine']['beverages'].items():
        try:
            BeverageFactory.get_beverage(beverage, composition)
            print('{} is prepared'.format(beverage))
        except Exception as e:
            print(e)
