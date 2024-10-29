"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    old=''
    dish_ingredients.sort()
    for dish_ingredient in dish_ingredients:
        if old == dish_ingredient:
            dish_ingredients.remove(dish_ingredient)
        old = dish_ingredient
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    for drink_ingredient in drink_ingredients:
        if drink_ingredient in ALCOHOLS:
            return drink_name + " Cocktail"
    return drink_name + " Mocktail"



def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """
    if dish_ingredients <= VEGAN:
        category = "VEGAN"
    elif dish_ingredients <= VEGETARIAN:
        category = "VEGETARIAN"
    elif dish_ingredients <= PALEO:
        category = "PALEO"
    elif dish_ingredients <= KETO:
        category = "KETO"
    else:
        category = "OMNIVORE"

    return f"{dish_name}: {category}"




def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    
    special_ingredients = {ingredient for ingredient in dish[1] if ingredient in SPECIAL_INGREDIENTS}
    return (dish[0], special_ingredients)
    

    pass


def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """
    ingredients = set()
    for dish in dishes:
        ingredients.update(dish)
    return ingredients

    pass


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    non_appetizers = [dish for dish in dishes if dish not in appetizers]
    return list(set(non_appetizers))  # Remove duplicatas se necessário

    pass


def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """
    singletons = (dish - intersection for dish in dishes)
    """
    # Criamos uma lista para armazenar ingredientes únicos de cada prato
    single_ingredient_sets = []

    # Passo 1: Iterar sobre cada prato da lista de pratos
    for dish in dishes:
        # Passo 2: Remover os ingredientes que estão na interseção comum
        unique_ingredients = dish - intersection

        # Passo 3: Adicionar o conjunto de ingredientes únicos desse prato à lista
        single_ingredient_sets.append(unique_ingredients)

    # Passo 4: Unir todos os conjuntos de ingredientes únicos para obter um conjunto final
    # contendo apenas os ingredientes que aparecem em um único prato
    all_singletons = set()
    for unique_set in single_ingredient_sets:
        all_singletons = all_singletons.union(unique_set)

    # Retorna o conjunto final de ingredientes únicos
    return all_singletons
    """

    return set.union(*singletons)