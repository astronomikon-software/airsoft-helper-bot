class Match:
    id: int
    name: str
    start_time: int
    duration: str
    place_name: str
    group_id: list[int]
    genre_id: list[int]
    is_loneliness_friendly: bool
    url: str
    annotation: str

    def __init__(
            self,
            id: int,
            name: str,
            start_time: int,
            duration: str,
            place_name: str,
            group_id: list,
            genre_id: list,
            is_loneliness_friendly: bool,
            url: str,
            annotation: str,
    ):
        self.id = id
        self.name = name
        self.start_time = start_time
        self.duration = duration
        self.place_name = place_name
        self.group_id = group_id
        self.genre_id = genre_id
        self.is_loneliness_friendly = is_loneliness_friendly
        self.url = url
        self.annotation = annotation
