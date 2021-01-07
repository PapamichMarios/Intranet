from app import db
from enums.role import RoleEnum
from model.genre import Genre
from model.role import Role


class ConfigurationService:

    @staticmethod
    def create_db_data():

        # create roles
        if not Role.query.all():
            admin_role = Role(id=1, name=RoleEnum.ROLE_ADMINISTRATOR.name, description='Admin Role')
            user_role = Role(id=2, name=RoleEnum.ROLE_USER.name, description='User Role')
            db.session.add(admin_role)
            db.session.add(user_role)

        # create genres
        if not Genre.query.all():
            horror = Genre(id=1, name='Horror', description='')
            thriller = Genre(id=2, name='Thriller', description='')
            drama = Genre(id=3, name='Drama', description='')
            comedy = Genre(id=4, name='Comedy', description='')

            db.session.add(horror)
            db.session.add(thriller)
            db.session.add(drama)
            db.session.add(comedy)

        db.session.commit()

