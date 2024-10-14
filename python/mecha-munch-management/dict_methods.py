"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1  # Incrementa a quantidade existente
        else:
            current_cart[item] = 1    # Adiciona o item com quantidade inicial de 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = {}
    for item in notes:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for recipe_name, ingredients_dict in recipe_updates:
        # Atualiza ou adiciona a receita no dicionário 'ideas'
        ideas[recipe_name] = ingredients_dict
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    cart_sorted = {}
    for item in sorted(cart):
        cart_sorted[item] = cart[item]
    return cart_sorted


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    # inicializa o carrinho de compras
    fulfillment_cart = {}

    # combina os itens do carrinho com as informações de corredor e refrigeração
    for item in cart:
        quantity = cart[item]
        aisle_info = aisle_mapping.get(item)

        if aisle_info:
            aisle, refrigeration = aisle_info
            fulfillment_cart[item] = [quantity, aisle, refrigeration]
        else:
            # Adiciona itens não encontrados no mapeamento de corredor
            continue

    # Retorna o carrinho de compras pronto para ser enviado à loja
    sorted_items = sorted(fulfillment_cart.items(), reverse=True)

    # Retorna o carrinho de compras pronto para ser enviado à loja
    sorted_fulfillment_cart = dict(sorted_items)

    return sorted_fulfillment_cart




def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item in fulfillment_cart:
        if item in store_inventory:
            ordered_quantity = fulfillment_cart[item][0]
            available_quantity, aisle, refrigeration = store_inventory[item]

            new_quantity = available_quantity - ordered_quantity

            if new_quantity > 0:
                store_inventory[item][0] = new_quantity
            else:
                store_inventory[item][0] = 'Out of Stock'
        else:
            continue

    return store_inventory

