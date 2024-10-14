"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    treasure, coordinate = record
    return coordinate


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    numero = ''.join(filter(str.isdigit, coordinate))
    letra = ''.join(filter(str.isalpha, coordinate))
    return (numero, letra)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    treasure, azara_coordinate = azara_record
    location, rui_coordinates, quadrant = rui_record

    # Converter rui_coordinates ('A', '1') em uma string 'A1'
    rui_coordinate_str = ''.join(rui_coordinates)

    return azara_coordinate == rui_coordinate_str




def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    # Passo 1: Desempacotar as tuplas
    treasure, azara_coordinate = azara_record
    location, rui_coordinate, quadrant = rui_record

    # Passo 2: Converter a coordenada de Rui para string
    rui_coordinate_str = ''.join(rui_coordinate)

    # Passo 3: Comparar as coordenadas
    if azara_coordinate != rui_coordinate_str:
        return "not a match"

    # **Passo 4: Combinar os registros (incluindo rui_coordinate)**
    combined_record = (treasure, azara_coordinate, location, rui_coordinate, quadrant)
    return combined_record



def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.
    """
    cleaned_records = []
    for record in combined_record_group:
        # Desempacotar o registro combinado com 5 elementos
        treasure, azara_coordinate, location, rui_coordinate, quadrant = record
        
        # Formatar o registro limpo como uma string
        # Removemos 'azara_coordinate' (excesso de informação)
        cleaned_record = f"({repr(treasure)}, {repr(location)}, {rui_coordinate}, {repr(quadrant)})"
        
        # Adicionar o registro limpo à lista
        cleaned_records.append(cleaned_record)
    
    # Unir todos os registros limpos em uma única string com quebras de linha e adicionar uma quebra de linha extra no final
    return '\n'.join(cleaned_records) + '\n'



