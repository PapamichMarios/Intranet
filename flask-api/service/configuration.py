from app import db, bcrypt, app
from enums.role import RoleEnum
from model.genre import Genre
from model.movie import Movie
from model.role import Role
from model.user import User


class ConfigurationService:

    @staticmethod
    def init_db_data():

        # create roles
        if not Role.query.first():
            admin_role = Role(id=1, name=RoleEnum.ROLE_ADMINISTRATOR.name, description='Admin Role')
            user_role = Role(id=2, name=RoleEnum.ROLE_USER.name, description='User Role')
            db.session.add(admin_role)
            db.session.add(user_role)

        # create genres
        if not Genre.query.first():
            horror = Genre(id=1, name='Horror', description='')
            thriller = Genre(id=2, name='Thriller', description='')
            drama = Genre(id=3, name='Drama', description='')
            comedy = Genre(id=4, name='Comedy', description='')
            crime = Genre(id=5, name='Crime', description='')
            animation = Genre(id=6, name='Animation', description='')

            db.session.add(horror)
            db.session.add(thriller)
            db.session.add(drama)
            db.session.add(comedy)
            db.session.add(crime)
            db.session.add(animation)

        # create admin
        if not User.query.first():
            password = bcrypt.generate_password_hash(app.config['ADMIN_PASSWORD']).decode('utf-8')
            admin = User(id=1,
                         username="admin",
                         password=password,
                         email="admin@admin",
                         first_name="Admin",
                         last_name="Admin")
            admin.roles = [Role.query.get(1)]

            db.session.add(admin)

        # create movies
        if not Movie.query.first():
            crime = Genre.query.filter(Genre.name == 'Crime').first()
            horror = Genre.query.filter(Genre.name == 'Horror').first()
            drama = Genre.query.filter(Genre.name == 'Drama').first()
            animation = Genre.query.filter(Genre.name == 'Animation').first()
            comedy = Genre.query.filter(Genre.name == 'Comedy').first()

            joker = Movie(id=1,
                          name="Joker",
                          year=2019,
                          duration=122,
                          description="In Gotham City, mentally troubled comedian Arthur Fleck is "
                                      "disregarded and mistreated by society. He then embarks on "
                                      "a downward spiral of revolution and bloody crime. This "
                                      "path brings him face-to-face with his alter-ego: the "
                                      "Joker.")

            joker.genres.append(crime)
            joker.genres.append(horror)
            joker.genres.append(drama)

            lion_king = Movie(id=2,
                              name="The Lion King",
                              year=1994,
                              duration=88,
                              description="Lion prince Simba and his father are targeted by his bitter uncle, "
                                          "who wants to ascend the thrfirst himself.")

            lion_king.genres.append(animation)
            lion_king.genres.append(drama)

            blackkklansman = Movie(id=3,
                                   name="BlacKkKlansman",
                                   year=2018,
                                   duration=135,
                                   description="Ron Stallworth, an African American police officer from Colorado "
                                               "Springs, CO, successfully manages to infiltrate the local Ku Klux "
                                               "Klan branch with the help of a Jewish surrogate who eventually "
                                               "becomes its leader. Based on actual events.")

            blackkklansman.genres.append(crime)
            blackkklansman.genres.append(comedy)

            db.session.add(joker)
            db.session.add(lion_king)
            db.session.add(blackkklansman)

        db.session.commit()
