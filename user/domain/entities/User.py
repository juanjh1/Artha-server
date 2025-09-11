from datetime import datetime


class User:
    def __init__(self, id: int, rank_id: int, score: int, completed_problems: int,
                 created_at: datetime, last_active: datetime,
                 avatar: str, status: bool, email: str, password: str)-> None:
        self.id = id
        self.rank_id = rank_id
        self.score = score
        self.completed_problems = completed_problems
        self.created_at = created_at
        self.last_active = last_active
        self.avatar = avatar
        self.status = status
        self.email = email
        self.password = password
