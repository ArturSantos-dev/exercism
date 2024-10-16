"""Functions which help the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param wagons: arbitrary number of wagon IDs.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagon IDs.
    :param missing_wagons: list - the list of missing wagon IDs.
    :return: list - corrected list of wagon IDs.
    """

    first_two = each_wagons_id[:2]
    remaining_wagons = each_wagons_id[2:]
    wagons = remaining_wagons + first_two


    locomotive_index = wagons.index(1)


    wagons = (
        wagons[:locomotive_index + 1]
        + missing_wagons
        + wagons[locomotive_index + 1:]
    )
    return wagons


def add_missing_stops(route, *args, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param args: arbitrary number of dictionaries with stops.
    :param kwargs: arbitrary number of stop keyword arguments.
    :return: dict - updated route dictionary.
    """
    stops = []


    for arg in args:
        if isinstance(arg, dict):
            stops.extend(arg.values())


    stops.extend(kwargs.values())

    route["stops"] = stops
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict - extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - corrected list of rows of wagons.
    """

    fixed_rows = [list(row) for row in zip(*wagons_rows)]
    return fixed_rows

