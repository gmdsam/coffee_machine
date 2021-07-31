from src.ingredients import *
from utils.utils import check_ingredients
import threading


class Formulae:
    """
    A class to define generic formulae for any beverage with predefined ingredients
    """
    def __init__(self):
        self.formulae = {
            'hot_milk': {
                'object': IngredientHotMilk(),
                'required_quantity': 0
            },
            'tea_leaves_syrup': {
                'object': IngredientTeaLeavesSyrup(),
                'required_quantity': 0
            },
            'ginger_syrup': {
                'object': IngredientGingerSyrup(),
                'required_quantity': 0
            },
            'sugar_syrup': {
                'object': IngredientSugarSyrup(),
                'required_quantity': 0
            },
            'elaichi_syrup': {
                'object': IngredientElaichiSyrup(),
                'required_quantity': 0
            },
            'coffee_syrup': {
                'object': IngredientCoffeeSyrup(),
                'required_quantity': 0
            },
            'hot_water': {
                'object': IngredientHotWater(),
                'required_quantity': 0
            }
        }


class BeverageFactory:
    """
    A factory class used to prepare beverages by creating Beverage objects, thereby hiding the beverage preparation
    logic
    """
    @staticmethod
    def get_beverage(beverage, composition):
        beverage_obj = Beverage()
        beverage_obj.set_formulae(composition)
        beverage_obj.update_beverage_ingredients(beverage)
        beverage_obj.prepare_beverage(beverage)


class Beverage:
    """
    Class which defines the formulae for a given beverage and uses it to deduct ingredients and prepare beverage
    accordingly
    """
    def __init__(self):
        self.__formulae = Formulae().formulae

    @property
    def formulae(self):
        return self.__formulae

    def set_formulae(self, config):
        """
        Defining required quantity of each ingredient for a given beverage. Also, defining new ingredient dynamically,
        not defined during initialization, to raise exceptions
        :param config: configuration of a given beverage
        """
        for ing_name in config:
            try:
                self.__formulae[ing_name]['required_quantity'] = config[ing_name] if ing_name in config else 0
            except KeyError:
                self.__formulae[ing_name] = {
                    'object': None,
                    'required_quantity': config[ing_name]
                }

    @staticmethod
    def prepare_beverage(beverage):
        print('Beverage {} is being prepared'.format(beverage))

    def update_beverage_ingredients(self, beverage):
        """
        Acquire lock, check whether ingredients are available and sufficient, and deduct quantity of each ingredient
        required to make the beverage. Raise exceptions whenever ingredient unavailable or insufficient
        :param beverage: name of the beverage
        """
        with threading.Lock():
            unavailable_ingredients, low_ingredients = check_ingredients(self.__formulae)
            if unavailable_ingredients:
                raise Exception('{} cannot be prepared because ingredient(s) {} is/are not available'.format(beverage, ', '.join(unavailable_ingredients)))
            if low_ingredients:
                raise Exception('{} cannot be prepared because ingredient(s) {} is/are not sufficient'.format(beverage, ', '.join(low_ingredients)))

            for ing_name, ingredient in self.__formulae.items():
                ingredient['object'].quantity -= ingredient['required_quantity']
            print('Ingredients obtained for {}'.format(beverage))
