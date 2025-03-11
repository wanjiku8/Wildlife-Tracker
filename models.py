from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Animal(Base):
    __tablename__ = "animals"
    id = Column(Integer, primary_key=True, index=True)
    species = Column(String, unique=True, nullable=False)
    habitat = Column(String, nullable=False)
    population = Column(Integer, nullable=False)

    sightings = relationship("Sighting", back_populates="animal")

class Sighting(Base):
    __tablename__ = "sightings"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)
    time = Column(DateTime, nullable=False)
    observer = Column(String, nullable=False)
    animal_id = Column(Integer, ForeignKey("animals.id"))

    animal = relationship("Animal", back_populates="sightings")