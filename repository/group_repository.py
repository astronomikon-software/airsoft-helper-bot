from model.group import Group
from data.read_all_execution import execute_read_query
from mapping.group_mapping import group_from_row


class GroupRepository:
    
    def read_all():
        rows = execute_read_query('''SELECT * from groups''')
        return list(map(group_from_row, rows))
