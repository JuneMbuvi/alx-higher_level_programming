#!/usr/bin/python3
"""python file that contains the class city"""
import sys
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """defines a class state that inherits from Base
    and links to sql table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    relationship('State')
