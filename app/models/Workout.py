from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    workoutName = Column(String(100), nullable=False)
    date = Column(String(10), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="workouts")

    exercises = relationship("Exercise", back_populates="workout")