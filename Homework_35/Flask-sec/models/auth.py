from database import db
from flask_security import UserMixin, RoleMixin
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

class RolesUsers(db.Model):
    __tablename__ = "roles_users"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("user.id"))
    role_id = Column(Integer(), ForeignKey("role.id"))


class Role(db.Model, RoleMixin):
    __tablename__ = "role"

    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = Column(Integer(), primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    active = Column(Boolean())
    fs_uniquifier = Column(String(255), unique=True, nullable=False)

    roles = relationship(
        "Role",
        secondary="roles_users",
        backref=backref("users", lazy="dynamic")
    )
