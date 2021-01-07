from app import db


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column('role_id', db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)

