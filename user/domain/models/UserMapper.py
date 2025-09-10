from user.domain.entities.User import User
from user.infrastructure.models import UserModel

class UserMapper:
    @staticmethod
    def to_entity(user_model: UserModel) -> User:
        return User(
            id=user_model.id,
            rank_id=user_model.rank.id if user_model.rank else None,
            score=user_model.score,
            completed_problems=user_model.completed_problems,
            created_at=user_model.created_at,
            last_active=user_model.last_active,
            avatar=user_model.avatar,
            status=user_model.status,
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
            created_at=user.created_at,
            last_active=user.last_active,
            avatar=user.avatar,
            status=user.status,
            email=user.email,
            password=user.password,
        )
