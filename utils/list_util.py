from model.place import Place


def place_from_name_row(row: tuple) -> Place:
    return Place(
        id=row[0],
        name=row[0],
    )
