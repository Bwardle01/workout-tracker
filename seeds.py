from app.models import User, Workout, Exercise, ExerciseStats
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


db = Session()

# insert users
db.add_all([
  User(username='Bronson', email='bronson@cbc.ca', password='bronson123'),
])

db.commit()

db.add_all([
  Workout(workoutName='Upper', date=1234, user_id=1 ),
])

db.commit()

db.add_all([
  Exercise(exerciseName='Db curl', workout_id=1),
])

db.commit()

db.add_all([
  ExerciseStats(weight='35', reps='15', exercise_id=1 ),
])

db.commit()

db.close()