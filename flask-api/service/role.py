from app import db
from model.role import Role


class RoleService:

    @staticmethod
    def find_by_role(role_key: str) -> Role:
        return Role.query.filter(Role.name == role_key).first()
