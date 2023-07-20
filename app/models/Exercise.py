from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True)
    exerciseName = Column(String(100), nullable=False)

    workout_id = Column(Integer, ForeignKey('workouts.id'))
    workout = relationship("Workout", back_populates="exercises")

    stats = relationship("ExerciseStats", back_populates="exercise")