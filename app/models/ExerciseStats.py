from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class ExerciseStats(Base):
    __tablename__ = 'exercise_stats'
    id = Column(Integer, primary_key=True)
    weight = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)

    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    exercise = relationship("Exercise", back_populates="stats")