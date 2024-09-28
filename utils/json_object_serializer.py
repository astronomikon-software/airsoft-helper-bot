from states_events.states import *
from model.match import Match


CLASSNAME_FIELD = '__classname__'
ENUM_FIELD = '__enumname__'


def serialize(obj):
    if obj is None:
        return None
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, bool):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, float):
        return obj
    elif isinstance(obj, list):
        return [
            serialize(value) for value in obj
        ]
    elif isinstance(obj, dict):
        return {
            key: serialize(value) for key, value in obj.items()
        }
    # elif isinstance(obj, Enum):
    #     return {
    #         ENUM_FIELD: serialize(value) for 
    #     }
    else:
        return {
            CLASSNAME_FIELD: obj.__class__.__name__,
        } | serialize(obj.__dict__)

  
def deserialize(obj):
    if obj is None:
        return None
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, bool):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, float):
        return obj
    elif isinstance(obj, list):
        return [
            deserialize(value) for value in obj
        ]
    elif isinstance(obj, dict):
        obj = {
            key: deserialize(value) for key, value in obj.items()
        }
        classname = obj.pop(CLASSNAME_FIELD, None)
        object_class = globals().get(classname, None)
        if object_class is not None:
            return object_class(**obj)
        else:
            return obj


"""
# Пример использования:

class Point:
    def __init__(
        self, 
        x: float,
        y: float,
    ):
        self.x = x
        self.y = y

class Point3(Point):
    def __init__(
        self, 
        x: float,
        y: float,
        z: float,
    ):
        Point.__init__(
            self,
            x = x,
            y = y,
        )
        self.z = z

class Location:
    def __init__(
        self, 
        id: int,
        name: str,
        points: list[Point],
    ):
        self.id = id
        self.name = name
        self.points = points

class User:
    def __init__(
        self, 
        id: int,
        name: str,
        is_admin: bool,
        location: Location,
        context: dict,
    ):
        self.id = id
        self.name = name
        self.is_admin = is_admin
        self.location = location
        self.context = context


json_dict = serialize(
    User(
        id=0,
        name='John',
        is_admin=True,
        location=Location(
            id=1,
            name='Opushka',
            points=[
                Point(x=0, y=0),
                Point3(x=0, y=1, z=2),
                Point(x=1, y=0),
                Point3(x=1, y=1, z=3),
            ],
        ),
        context={
            'a': 'A',
            'b': 1,
            'c': True,
            'd': 1.27,
            'e': ['E', 'E', 'E'],
            'f': {
                'what': '??',
            },
        }
    ),
)

obj = deserialize(json_dict)
"""    
