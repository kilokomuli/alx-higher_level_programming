#!/usr/bin/python3
"""Defines a state model, inherits from SQLAlchemy Base and links
to the MySQL table states"""
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Defines state class and links to the MySQL table states"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
