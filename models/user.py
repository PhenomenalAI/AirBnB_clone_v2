#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import Column


class User(BaseModel, Base):
	"""Represents a user for a MySQL database."""
	__tablename__ = "users"
	email = Column(String(128), nullable=False)
	password = Column(String(128), nullable=False)
	first_name = Column(String(128))
	last_name = Column(String(128))
