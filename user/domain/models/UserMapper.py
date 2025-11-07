from user.domain.entities.User import User
from user.infrastructure.models import UserModel


class UserMapper:
    @staticmethod
    def to_entity(user_model: UserModel) -> User:
        return User(
            id=user_model.id, #type: ignore[attr-defined]
            rank_id=user_model.rank.id, #type: ignore[attr-defined]
            score=user_model.score,
            completed_problems=user_model.completed_problems,
            avatar=user_model.avatar,
            email=user_model.email,
            password=user_model.password,
        )

    @staticmethod
    def to_model(user: User) -> UserModel:
        return UserModel(
            id=user.id,
            rank_id=user.rank_id,
            score=user.score,
            completed_problems=user.completed_problems,
            avatar=user.avatar,
            email=user.email,
            password=user.password,
        )
