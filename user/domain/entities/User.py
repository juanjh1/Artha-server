from dataclasses import dataclass


@dataclass
class User:
    id: int
    rank_id: int
    score: int
    completed_problems: int
    avatar: str
    email: str
    password: str
