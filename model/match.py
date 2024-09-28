class Match:
    id: int
    start_time: int
    place_id: int
    group_id: int
    genre_id: int
    is_loneliness_friendly: bool
    url: str

    def __init__(
            self,
            id: int,
            start_time: int,
            place_id: int,
            group_id: int,
            genre_id: int,
            is_loneliness_friendly: bool,
            url: str,
    ):
        self.id = id
        self.start_time = start_time
        self.place_id = place_id
        self.group_id = group_id
        self.genre_id = genre_id
        self.is_loneliness_friendly = is_loneliness_friendly
        self.url = url
