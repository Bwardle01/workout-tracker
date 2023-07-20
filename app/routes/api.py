import sys
from flask import Blueprint, request, jsonify, session
from app.models import User, Exercise, Workout, ExerciseStats
from app.db import get_db
# from app.utils.auth import login_required this is a util

bp = Blueprint('api', __name__, url_prefix='/api')


# signup
@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db()

  try:
    # attempt creating a new user
    newUser = User(
      username = data['username'],
      email = data['email'],
      password = data['password']
    )

    db.add(newUser)
    db.commit()
  except:
    print(sys.exc_info()[0])

    # insert failed, so rollback and send error to front end
    db.rollback()
    return jsonify(message = 'Signup failed'), 500

  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True

  return jsonify(id = newUser.id)

# logout
@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

# login
@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()

  try:
    user = db.query(User).filter(User.email == data['email']).one()
  except:
    print(sys.exc_info()[0])

    return jsonify(message = 'Incorrect credentials'),400

  if user.verify_password(data['password']) == False:
    return jsonify(message = 'Incorrect credentials'),400

  session.clear()
  session['user_id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)

# save data route
@bp.route('/save', methods=['POST'])
def save_workout_dats():
    data = request.get_json()
    workout_data = data.get('data',{})
    print('Received data:', data)
    db = get_db()

    try:
        # Get user_id from the session if logged in
        user_id = session.get('user_id')
        if user_id:
            user = db.query(User).get(user_id)
            if not user:
                return jsonify(message='User not found'), 404
        else:
            return jsonify(message='User not logged in'), 401

        workout_name = data.get('workoutName')
        workout_date = data.get('date')
        exercises_data = [workout_data]

        # Create a new workout for the user
        new_workout = Workout(name=workout_name, date=workout_date, user=user)
        db.add(new_workout)
        db.commit()

        # Add exercises and their stats to the workout
        for exercise_data in exercises_data:
            exercise_name = exercise_data.get('exerciseName')
            weight = exercise_data.get('weight')
            reps = exercise_data.get('reps')

            print('Exercise:', exercise_name, 'Weight:', weight, 'Reps:', reps)


            exercise = Exercise(name=exercise_name, workout=new_workout)
            db.add(exercise)
            db.commit()

            stats = ExerciseStats(weight=weight, reps=reps, exercise=exercise)
            db.add(stats)
            db.commit()

        return jsonify(message='Data saved successfully')
    except Exception as e:
        print(sys.exc_info()[0])
        db.rollback()
        return jsonify(error='Failed to save data: {}'.format(str(e))), 500
