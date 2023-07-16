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
  Workout(name='Upper', date='01/01/01' ),
])

db.commit()

db.add_all([
  Exercise(name='Db curl'),
])

db.commit()

db.add_all([
  ExerciseStats(weight='35', reps='15'),
])

db.commit()

db.close()