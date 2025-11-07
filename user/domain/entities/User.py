

class User:
    def __init__(self, id: int, rank_id: int, score: int, completed_problems: int,
                 avatar: str, email: str, password: str)-> None:
        self.id = id
        self.rank_id = rank_id
        self.score = score
        self.completed_problems = completed_problems
        self.avatar = avatar
        self.email = email
        self.password = password
