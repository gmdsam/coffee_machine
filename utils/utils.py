def check_ingredients(formulae):
    """
    Validate if ingredients required to prepare a beverage are available and in sufficient quantity
    :param formulae: a dictionary to hold ingredient objects and quantity required for each ingredient to prepare a
                     particular beverage
    :return: list of unavailable ingredients and ingredients running low
    """
    unavailable_ingredients = []
    low_ingredients = []
    for ing_name, ingredient in formulae.items():
        if ingredient['required_quantity'] > 0:
            if ingredient['object'] is None:
                unavailable_ingredients.append(ing_name)
            elif ingredient['object'].quantity < ingredient['required_quantity']:
                low_ingredients.append(ing_name)
    return unavailable_ingredients, low_ingredients
