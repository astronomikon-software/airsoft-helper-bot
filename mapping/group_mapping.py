from model.group import Group


def group_from_row(row: tuple) -> Group:
    group = group()
    group.id = row[0]
    group.name = row[1]
    return group

def row_from_group(group: Group) -> tuple:
    row = (group.id, group.name)
    return row
