from abc import ABC, abstractmethod
from utils.singleton import singleton
from utils.constant import ingredient_threshold


class Ingredient(ABC):
    """
    An abstract class that will be derived by each ingredient class we define statically for our coffee machine. It has
    property method, setter method and a method to check whether quantity of any ingredient is low based on predefined
    threshold
    """
    @abstractmethod
    def __init__(self, quantity, threshold):
        self.__quantity = quantity
        self.__threshold = threshold

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    def is_low(self):
        return self.__quantity < self.__threshold


@singleton
class IngredientHotMilk(Ingredient):
    """
    Class for hot milk that derives abstract class Ingredient and uses its methods
    """
    def __init__(self, quantity, threshold):
        super().__init__(quantity, threshold)


@singleton
class IngredientTeaLeavesSyrup(Ingredient):
    def __init__(self, quantity, threshold):
        super().__init__(quantity, threshold)


@singleton
class IngredientGingerSyrup(Ingredient):
    def __init__(self, quantity, threshold):
        super().__init__(quantity, threshold)


@singleton
class IngredientSugarSyrup(Ingredient):
    def __init__(self, quantity, threshold):
        super().__init__(quantity, threshold)


@singleton
class IngredientElaichiSyrup(Ingredient):
    def __init__(self, quantity, threshold):
        super().__init__(quantity, threshold)


@singleton
class IngredientCoffeeSyrup(Ingredient):
    def __init__(self, quantity, threshold):
        super().__init__(quantity, threshold)


@singleton
class IngredientHotWater(Ingredient):
    def __init__(self, quantity, threshold):
        super().__init__(quantity, threshold)


class InitializeIngredients:
    """
    Initialize all statically defined ingredients with quantity given in input. If an ingredient is not available in
    input, its quantity will be set to 0
    """
    def __init__(self, ingredients):
        IngredientHotMilk(ingredients['hot_milk'] if 'hot_milk' in ingredients else 0,
                          ingredient_threshold['hot_milk'])
        IngredientTeaLeavesSyrup(ingredients['tea_leaves_syrup'] if 'tea_leaves_syrup' in ingredients else 0,
                                 ingredient_threshold['tea_leaves_syrup'])
        IngredientGingerSyrup(ingredients['ginger_syrup'] if 'ginger_syrup' in ingredients else 0,
                              ingredient_threshold['ginger_syrup'])
        IngredientSugarSyrup(ingredients['sugar_syrup'] if 'sugar_syrup' in ingredients else 0,
                             ingredient_threshold['sugar_syrup'])
        IngredientElaichiSyrup(ingredients['elaichi_syrup'] if 'elaichi_syrup' in ingredients else 0,
                               ingredient_threshold['elaichi_syrup'])
        IngredientCoffeeSyrup(ingredients['coffee_syrup'] if 'coffee_syrup' in ingredients else 0,
                              ingredient_threshold['coffee_syrup'])
        IngredientHotWater(ingredients['hot_water'] if 'hot_water' in ingredients else 0,
                           ingredient_threshold['hot_water'])
