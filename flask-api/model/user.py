from app import db
import model.role

user_roles_table = db.Table('user_has_roles', db.Model.metadata,
                            db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
                            db.Column('role_id', db.Integer, db.ForeignKey('role.role_id')))


class User(db.Model):
    __tablename__ = "user"
    id = db.Column('user_id', db.Integer, primary_key=True, index=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    roles = db.relationship('Role', secondary=user_roles_table)
