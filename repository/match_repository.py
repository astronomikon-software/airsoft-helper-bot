from model.match import Match


class match_repository:

    async def create(self) -> Match:
        pass
    
    async def update(self, match: Match):
        pass

    async def delete(self, match: Match):
        pass

    async def read_all(self, match: Match):
        pass

    async def filter_by_genre(self) -> list[Match]:
        pass

    async def filter_by_place(self) -> list[Match]:
        pass

    async def filter_by_group(self) -> list[Match]:
        pass

    async def filter_by_solo_friendliness(self) -> list[Match]:
        pass

